from motor.motor_asyncio import AsyncIOMotorClient
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017"
    # CILENT = AsyncIOMotorClient(MONGO_URL)
    TODO_DB_NAME: str = "todo_db"
    TASKS_COLLECTION: str = "tasks"

settings = Settings()


