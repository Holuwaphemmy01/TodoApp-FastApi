# from pydantic import BaseModel
# from typing import Optional, List
# from bson import ObjectId
# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
#
# class TaskBase(BaseModel):
#     title: str
#     completed: bool = False
#
# class TaskCreate(TaskBase):
#     pass
#
# class TaskUpdate(BaseModel):
#     title: Optional[str] = None
#     completed: Optional[bool] = None
#
# class TaskResponse(TaskBase):
#     id: str
#
#     class Config:
#         orm_mode = True
#         json_encoders = {
#             ObjectId: str
#         }

from pydantic import BaseModel, ConfigDict
from typing import Optional
from bson import ObjectId

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(TaskBase):
    id: str
    model_config = ConfigDict(
        from_attributes=True,
        # json_encoders={ObjectId: str}
    )