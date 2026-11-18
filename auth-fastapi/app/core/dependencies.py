from fastapi import Cookie, HTTPException
from bson import ObjectId
import jwt
from bson.errors import InvalidId
from app.core.security import decode_access_token
from app.db.mongodb import users_collection






def get_current_user(access_token:str |None = Cookie(default=None))->dict:
    if access_token is None:
        raise HTTPException(status_code=401, detail="Unauthorize")
    try:
        payload = decode_access_token(access_token)
        user_id = payload["sub"]
        user = users_collection.find_one({"_id":ObjectId(user_id)})
    except (jwt.PyJWTError , InvalidId, KeyError):
        raise HTTPException(status_code=401,detail="invalid or expired token")
    if not user:
        raise HTTPException(status_code="401" ,detail="user not found")
    
    return user