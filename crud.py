# crud.py
from database import collection
from models import TaskCreate, TaskUpdate, TaskResponse
from bson import ObjectId
from typing import List

async def get_task_or_404(task_id: str):
    task = await collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Task not found")
    return task

async def get_all_tasks() -> List[TaskResponse]:
    tasks = []
    async for task in collection.find({}):
        tasks.append(TaskResponse(id=str(task["_id"]), **task))
    return tasks

async def create_new_task(task: TaskCreate) -> TaskResponse:
    new_task = task.dict()
    result = await collection.insert_one(new_task)
    created_task = await collection.find_one({"_id": result.inserted_id})
    return TaskResponse(id=str(created_task["_id"]), **created_task)

async def update_existing_task(task_id: str, task_update: TaskUpdate) -> TaskResponse:
    task = await get_task_or_404(task_id)
    update_data = task_update.dict(exclude_unset=True)
    await collection.update_one({"_id": task["_id"]}, {"$set": update_data})
    updated_task = await collection.find_one({"_id": task["_id"]})
    return TaskResponse(id=str(updated_task["_id"]), **updated_task)

async def delete_existing_task(task_id: str):
    task = await get_task_or_404(task_id)
    await collection.delete_one({"_id": task["_id"]})