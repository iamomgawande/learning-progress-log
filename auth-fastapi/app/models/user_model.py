from typing import Annotated
from pydantic import BaseModel, BeforeValidator, EmailStr, Field

PyObjectId = Annotated[str, BeforeValidator(str)]   # ObjectId -> str

class CreateUser(BaseModel):
    full_name:str | None = None
    email:EmailStr
    password:str = Field(min_length=8)


class UserOut(BaseModel):
    id:PyObjectId = Field(alias="_id")
    full_name:str | None = None
    email:EmailStr



class UserLogin(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8)
    