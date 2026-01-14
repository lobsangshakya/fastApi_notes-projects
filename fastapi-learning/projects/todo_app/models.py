from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False


class TodoIn(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    created_at: datetime = datetime.now()