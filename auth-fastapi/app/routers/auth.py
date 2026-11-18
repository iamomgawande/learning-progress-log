from fastapi import FastAPI,Depends, HTTPException ,Response,APIRouter
from app.db.mongodb import users_collection
from app.models.user_model import CreateUser, UserOut, UserLogin
from app.core.security import hash_password, verify_password , create_access_token
from app.core.config import settings


router = APIRouter()

@router.post(
    "/register",
    status_code=201,
    response_model=UserOut,
    response_model_by_alias=False,
)
def register_user(user: CreateUser):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=409, detail="Email already registered")

    data = user.model_dump()
    data["password"] = hash_password(data["password"])
    result = users_collection.insert_one(data)
    data["id"] = result.inserted_id
    return data


@router.post("/login")
def login_user(credentials: UserLogin,response:Response):
    db_user = users_collection.find_one({"email": credentials.email})
    if db_user is None or not verify_password(credentials.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")


    access_token = create_access_token(str(db_user["_id"]))
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,                     
        secure=False,                     
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )
    return {"message": "Login Successful"}


@router.post("/logout")
def logout_user(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}