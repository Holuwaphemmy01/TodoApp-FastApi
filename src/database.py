from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client[settings.TODO_DB_NAME]
collection = db[settings.TASKS_COLLECTION]

