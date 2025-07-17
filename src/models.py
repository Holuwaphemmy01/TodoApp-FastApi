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