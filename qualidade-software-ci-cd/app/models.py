# app/models.py
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool = False
