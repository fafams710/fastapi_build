from threading import Lock
from itertools import islice

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI()





class Notes(BaseModel):
    note: str = Field(min_length=1, max_length=200)

class Noteread(BaseModel):
    id: int
    note: str 


NOTES: dict[int, Noteread] = {}

NEXT_ID = 1

NOTES_LOCK = Lock()


@app.post("/events", status_code=201)
def create_note(body: Notes) -> Noteread:
    global NEXT_ID

    with NOTES_LOCK:
        new_note = Noteread(
            id=NEXT_ID,
            note=body.note,
        )
        NOTES[NEXT_ID] = new_note
        NEXT_ID += 1

    return new_note

@app.get("/events")
def list_notes(
    limit: int = Query(default=10, ge=0),
) -> list[Noteread]:
    
    with NOTES_LOCK:
        return list(islice(reversed(NOTES.values()), limit))

@app.get("/events/{note_id}")
def read_note(note_id: int) -> Noteread:

    with NOTES_LOCK:
        note = NOTES.get(note_id)

    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note