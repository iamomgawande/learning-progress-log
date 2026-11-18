from pydantic import BaseModel,Field
class NoteCreate(BaseModel):
    title:str=Field(min_length=1, max_length=200)
    content:str=""
    tags:list[str]=Field(default_factory=list)


class NoteOut(NoteCreate):
    id:str