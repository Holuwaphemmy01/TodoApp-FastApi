from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017"
    TODO_DB_NAME: str = "todo_db"
    TASKS_COLLECTION: str = "tasks"

settings = Settings()


