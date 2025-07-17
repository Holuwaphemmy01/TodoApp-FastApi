# db_utils.py
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client[settings.TODO_DB_NAME]
collection = db[settings.TASKS_COLLECTION]