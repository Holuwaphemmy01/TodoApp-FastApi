from http.client import HTTPException

from bson import ObjectId

from main import collection


async def get_task_or_404(task_id: str):

    task = await collection.find_one(({"_id": ObjectId(task_id)})

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task;


