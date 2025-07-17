from fastapi import APIRouter, Depends, HTTPException
from models import TaskCreate, TaskUpdate, TaskResponse
from crud import get_all_tasks, create_new_task, update_existing_task, delete_existing_task
from typing import List

router = APIRouter()

@router.get("/tasks", response_model=List[TaskResponse])
async def list_tasks():
    return await get_all_tasks()

@router.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(task: TaskCreate):
    return await create_new_task(task)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: str):
    return await get_all_tasks()[next((i for i, t in enumerate(await get_all_tasks()) if t.id == task_id), -1)]

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: str, task_update: TaskUpdate):
    return await update_existing_task(task_id, task_update)

@router.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: str):
    await delete_existing_task(task_id)
    return None