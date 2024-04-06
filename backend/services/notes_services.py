from utils.database_utils import (
    get_number_of_notes as db_get_number_of_notes,
    get_notes as db_get_notes,
    get_note as db_get_note,
    add_note as db_add_note,
    delete_note as db_delete_note,
)
from config.init_config import get_config
from fastapi import HTTPException


def init_notes():
    # Init the notes service

    # Create few notes if the notes collection is empty
    if db_get_number_of_notes() == 0:
        create_note(
            "Things to do",
            "Buy milk",
        )
        create_note(
            "Ideas",
            "Create a new app",
        )
        create_note(
            "Books to read",
            "The Pragmatic Programmer",
        )


def get_notes():
    # Get the notes list
    return db_get_notes()


def get_note(note_id):
    # Get a specific note
    note = db_get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


def create_note(title, content):
    # Verify the input
    config = get_config()
    NOTES_NUMBER_MAX = config["NOTES"]["NOTES_NUMBER_MAX"]
    NOTES_TITLE_LENGTH_MAX = config["NOTES"]["NOTES_TITLE_LENGTH_MAX"]
    NOTES_CONTENT_LENGTH_MAX = config["NOTES"]["NOTES_CONTENT_LENGTH_MAX"]

    if len(title) > NOTES_TITLE_LENGTH_MAX:
        raise HTTPException(
            status_code=400,
            detail=f"Title is too long (max {NOTES_TITLE_LENGTH_MAX} characters)",
        )

    if len(content) > NOTES_CONTENT_LENGTH_MAX:
        raise HTTPException(
            status_code=400,
            detail=f"Content is too long (max {NOTES_CONTENT_LENGTH_MAX} characters)",
        )

    # Check the number of notes
    number_of_notes = db_get_number_of_notes()
    if number_of_notes > NOTES_NUMBER_MAX:
        raise HTTPException(
            status_code=402,
            detail=f"Too many notes (max {NOTES_NUMBER_MAX})",
        )

    # Create the note
    note = {
        "title": title,
        "content": content,
    }

    note_id = db_add_note(note)
    note["id"] = note_id

    return note


def delete_note(note_id):
    # Delete a note
    note = db_get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    db_delete_note(note_id)
