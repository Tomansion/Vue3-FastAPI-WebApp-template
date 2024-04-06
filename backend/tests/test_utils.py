from utils.database_utils import (
    setup as setup_database,
    empty_collection_by_name,
    delete_collection_by_name,
)

NOTES_COLLECTION_NAME = "notes_test"


def setup_test_database():
    setup_database(notes_collection_name=NOTES_COLLECTION_NAME)
    empty_collection_by_name(NOTES_COLLECTION_NAME)


def delete_test_database():
    delete_collection_by_name(NOTES_COLLECTION_NAME)
