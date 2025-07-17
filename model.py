from typing import Optional
from bson import ObjectId

import pydantic
from pydantic.v1 import BaseModel


class TaskBase (BaseModel):
    title: str
    description: str

class TaskCreate (TaskBase):
    pass

class TaskUpdate (BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse (TaskBase):
    id: str

    class Config:
        orm_mode = True
        json_encoders = {
            objectId: str
        }
