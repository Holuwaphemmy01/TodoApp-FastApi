from asyncio import tasks

from fastapi import FastAPI
from src.routes import router

app = FastAPI()

app.include_router(router, prefix="/api")
print("Welcome")



@app.get("/")
async def root():
    return {"message": "Hello World"}




#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
