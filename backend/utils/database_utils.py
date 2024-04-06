from config.init_config import get_config, DEBUG_COLOR, ERROR_COLOR
from termcolor import colored
from arango import ArangoClient, exceptions
from typing import Optional, List

db = None  # Wrapper for the Arango database

NOTES_COLLECTION_NAME = "notes"


def setup(notes_collection_name=None):
    global db, NOTES_COLLECTION_NAME

    # Set the collection names
    if notes_collection_name is not None:
        NOTES_COLLECTION_NAME = notes_collection_name

    # Load config
    config = get_config()
    HOST = config["ARANGODB"]["HOST"]
    PORT = config["ARANGODB"]["PORT"]
    DATABASE = config["ARANGODB"]["DATABASE"]
    USER = config["ARANGODB"]["USER"]
    PASSWORD = config["ARANGODB"]["PASSWORD"]

    print("\nConnecting to ArangoDB...")
    print(f" - Host: {colored(HOST, DEBUG_COLOR)}")
    print(f" - Port: {colored(PORT, DEBUG_COLOR)}")
    print(f" - Database: {colored(DATABASE, DEBUG_COLOR)}")
    print(f" - User: {colored(USER, DEBUG_COLOR)}")

    # Initialize the ArangoDB client
    client = ArangoClient(hosts=f"http://{HOST}:{PORT}", resolver_max_tries=1)

    # Connect to the database
    db = client.db(DATABASE, username=USER, password=PASSWORD)

    # Test that the connection was successful
    try:
        version = db.version()
        print(
            f" - Connection to Arango {colored('Arango '+ version, DEBUG_COLOR)} established"
        )
    except ConnectionAbortedError:
        print(" -", colored("Connection failed", ERROR_COLOR))

        raise ConnectionAbortedError(
            colored(f"Failed to connect to ArangoDB at {HOST}:{PORT}", ERROR_COLOR)
        )

    # Create the notes collection if it doesn't exist
    _create_collection_by_name(NOTES_COLLECTION_NAME)


# Wrapper
def db_must_be_setup(func):
    def wrapper_db_must_be_setup(*args, **kwargs):
        if db is None:
            raise Exception("Database not setup")
        return func(*args, **kwargs)

    return wrapper_db_must_be_setup


# Collection utils
@db_must_be_setup
def _create_collection_by_name(collection_name):
    if not db.has_collection(collection_name):
        print(f" - Creating collection {colored(collection_name, DEBUG_COLOR)}")
        db.create_collection(collection_name)


@db_must_be_setup
def empty_collection_by_name(collection_name):
    if db.has_collection(collection_name):
        print(f" - Emptying collection {colored(collection_name, DEBUG_COLOR)}")
        db.collection(collection_name).truncate()


@db_must_be_setup
def delete_collection_by_name(collection_name):
    if db.has_collection(collection_name):
        print(f" - Deleting collection {colored(collection_name, DEBUG_COLOR)}")
        db.delete_collection(collection_name)


# Notes functions
@db_must_be_setup
def get_number_of_notes() -> int:
    # Get the number of notes in the database
    return db.collection(NOTES_COLLECTION_NAME).count()


@db_must_be_setup
def get_notes() -> List[dict]:
    # Get all the notes in the database
    notes = list(db.collection(NOTES_COLLECTION_NAME).all())
    for note in notes:
        note["id"] = note["_key"]
    return notes


@db_must_be_setup
def get_note(note_id) -> Optional[dict]:
    print(f" - Getting note {colored(note_id, DEBUG_COLOR)}")
    note = db.collection(NOTES_COLLECTION_NAME).get(note_id)
    if note is not None:
        note["id"] = note["_key"]
        return note


@db_must_be_setup
def add_note(note) -> str:
    res = db.collection(NOTES_COLLECTION_NAME).insert(note, overwrite=True)
    return res["_key"]


@db_must_be_setup
def delete_note(note_id) -> bool:
    try:
        db.collection(NOTES_COLLECTION_NAME).delete(note_id)
        return True
    except exceptions.DocumentDeleteError:
        # The note doesn't exist
        return False
