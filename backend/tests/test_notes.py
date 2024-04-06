import pytest
from fastapi import HTTPException

from utils.database_utils import (
    get_number_of_notes as db_get_number_of_notes,
    get_notes as db_get_notes,
    get_note as db_get_note,
)
import services.notes_services as notes_service
from config.init_config import get_config
from tests.test_utils import setup_test_database, delete_test_database


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    setup_test_database()
    config = get_config()
    yield config
    delete_test_database()


def test_init_notes():
    notes_service.init_notes()
    assert db_get_number_of_notes() == 3


def test_get_notes():
    notes = notes_service.get_notes()
    assert len(notes) == 3


def test_get_note():
    notes = notes_service.get_notes()
    note = notes_service.get_note(notes[0]["id"])
    assert note is not None
    assert note["title"] == "Things to do"


def test_get_non_existent_note():
    with pytest.raises(HTTPException) as e:
        notes_service.get_note("non_existent_id")
    assert str(e.value.detail) == "Note not found"


def test_create_note():
    new_note = notes_service.create_note(
        title="New Note", content="This is a new note."
    )
    assert db_get_number_of_notes() == 4
    notes = db_get_notes()
    assert notes[-1]["title"] == "New Note"
    assert notes[-1]["content"] == "This is a new note."
    assert notes[-1]["id"] == new_note["id"]


def test_delete_note():
    notes = notes_service.get_notes()
    note = notes_service.get_note(notes[0]["id"])
    notes_service.delete_note(note["id"])
    assert db_get_number_of_notes() == 3
    assert db_get_note(note["id"]) is None


def test_delete_non_existent_note():
    with pytest.raises(HTTPException) as e:
        notes_service.delete_note("non_existent_id")
    assert str(e.value.detail) == "Note not found"


def test_create_note_invalid_title(setup_module):
    config = setup_module
    NOTES_TITLE_LENGTH_MAX = config["NOTES"]["NOTES_TITLE_LENGTH_MAX"]

    with pytest.raises(HTTPException) as e:
        notes_service.create_note(
            "X" * (NOTES_TITLE_LENGTH_MAX + 1), "This is a new note."
        )
    assert "Title is too long" in str(e.value.detail)
    assert str(NOTES_TITLE_LENGTH_MAX) in str(e.value.detail)


def test_create_note_invalid_content(setup_module):
    config = setup_module
    NOTES_CONTENT_LENGTH_MAX = config["NOTES"]["NOTES_CONTENT_LENGTH_MAX"]

    with pytest.raises(HTTPException) as e:
        notes_service.create_note("New Note", "X" * (NOTES_CONTENT_LENGTH_MAX + 1))
    assert "Content is too long" in str(e.value.detail)
    assert str(NOTES_CONTENT_LENGTH_MAX) in str(e.value.detail)


def test_max_notes(setup_module):
    config = setup_module
    NOTES_NUMBER_MAX = config["NOTES"]["NOTES_NUMBER_MAX"]

    while db_get_number_of_notes() <= NOTES_NUMBER_MAX:
        notes_service.create_note("Test Note", "This is a test note.")

    with pytest.raises(HTTPException) as e:
        notes_service.create_note("Another Note", "This is another test note.")

    assert "Too many notes" in str(e.value.detail)
    assert str(NOTES_NUMBER_MAX) in str(e.value.detail)
