from fastapi import FastAPI
from app.routers import auth,user




app = FastAPI()

app.include_router(auth.router)

app.include_router(user.router)


@app.get("health")
def health():
    return {"message":"OK"}

