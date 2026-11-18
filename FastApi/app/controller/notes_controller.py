from app.database import db
from app.schemas import note

def getAllNotes():
        notes = list(db.notes.find())
        for note in notes:
                note["_id"] = str(note["_id"])
        return notes



        