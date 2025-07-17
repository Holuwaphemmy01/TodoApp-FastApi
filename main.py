from asyncio import tasks

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routes import router

app = FastAPI()


MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client.todo_db
collection = db.tasks


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix='/api')



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
