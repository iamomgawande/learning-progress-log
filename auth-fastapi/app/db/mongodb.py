from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(
    settings.MONGO_URL,
    serverSelectionTimeoutMS=5000
)

db = client[settings.MONGO_DB]
users_collection = db["users"]