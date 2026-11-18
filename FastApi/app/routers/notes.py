from fastapi import APIRouter
from app.controller import notes_controller
router = APIRouter(prefix="/notes",tags=["Notes"])


@router.get('/')
def get_note():
    return notes_controller.getAllNotes()

@router.get('/{note_id}')
def get_note_by_id(note_id:str):
    return {"id":note_id,"message":"note id recived"}