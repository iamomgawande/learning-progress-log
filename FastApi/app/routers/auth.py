from fastapi import APIRouter

router = APIRouter(prefix="/user",tags=['User'])


@router.get('/')
def get_user():
    return{"message":"all user will be here "}