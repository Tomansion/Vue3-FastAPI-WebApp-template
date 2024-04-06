from services.notes_services import (
    get_notes as get_notes_service,
    get_note as get_note_service,
    create_note as create_note_service,
    delete_note as delete_note_service,
)
from utils.socket_utils import connection_manager

from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List

router = APIRouter()


class NoteCreation(BaseModel):
    title: str = Field(
        ..., example="Things to do", description="The note title", min_length=1
    )
    content: str = Field(..., example="Buy milk", description="The note content")


class Note(NoteCreation):
    id: str = Field(..., description="The note ID")


#############################################################################
# Notes API
#############################################################################


@router.get("/notes", response_model=List[Note], tags=["Notes"])
def get_notes():
    # Get the notes list
    return get_notes_service()


@router.get("/notes/{note_id}", response_model=Note, tags=["Notes"])
def get_note(note_id):
    # Get a specific note
    return get_note_service(note_id)


@router.post("/notes", response_model=Note, tags=["Notes"])
async def create_note(body: NoteCreation):
    # Create the notes
    created_note = create_note_service(
        body.title,
        body.content,
    )

    # Broadcast the note creation
    await connection_manager.broadcast({"noteCreationUpdate": created_note})

    return created_note


@router.delete("/notes/{note_id}", tags=["Notes"])
async def delete_note(note_id):
    # Delete a note
    delete_note_service(note_id)

    # Broadcast the note deletion
    await connection_manager.broadcast({"noteDeletionUpdate": note_id})
