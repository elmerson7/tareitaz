from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---------- USER ----------
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ---------- TASK ----------
class TaskBase(BaseModel):
    title: str
    status: Optional[str] = "pendiente"
    progress: Optional[int] = 0

class TaskCreate(TaskBase):
    user_id: int

class TaskOut(TaskBase):
    id: int
    created_at: datetime
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    user_id: int

    class Config:
        orm_mode = True
