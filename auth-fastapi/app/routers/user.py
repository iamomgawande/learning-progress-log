from fastapi import Depends, HTTPException,APIRouter
from bson import ObjectId
from bson.errors import InvalidId
from app.db.mongodb import users_collection
from app.models.user_model import UserOut
from app.core.config import settings
from app.core.dependencies import get_current_user


router = APIRouter()


@router.get('/me' , response_model=UserOut, response_model_by_alias=False)
def get_current_user(current_user:dict = Depends(get_current_user)):
    return current_user

@router.get("/users", response_model=list[UserOut], response_model_by_alias=False)
def get_users(page:int = 1, limit:int = 10, current_user:dict = Depends(get_current_user)):
    skip= (page -1) * limit
    return list(users_collection.find().skip(skip).limit(limit))


@router.get("/users/{user_id}", response_model=UserOut, response_model_by_alias=False)
def get_user_by_id(user_id: str):
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user id")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
