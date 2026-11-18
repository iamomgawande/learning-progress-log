from fastapi import FastAPI, HTTPException
from app.schemas.note import NoteCreate,NoteOut
from app.database import db
from app.routers import notes
from app.routers import auth
app = FastAPI()


app.include_router(notes.router)
app.include_router(auth.router)
notes :list[dict] = []
next_id = 1


# @app.get("/notes")
# def get_notes():
#     return notes

# @app.get("/notes/{note_id}",response_model=NoteOut)
# def get_note_by_id(note_id:int):
#     for note in notes:
#         if note["id"] == note_id:
#             return note

#     raise HTTPException(status_code=404, detail= "Note not found")


# @app.post("/notes",status_code=201, response_model=NoteOut)
# def create_note(note:NoteCreate):
#     new_note = note.model_dump()
#     result = db.notes.insert_one(new_note)
#     return {"id":str(result.inserted_id),**new_note}


@app.get("/health")
def health():
    return {
        "status":"ok"
    }