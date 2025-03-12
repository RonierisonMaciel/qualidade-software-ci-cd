# app/main.py

from fastapi import FastAPI, HTTPException
from app.models import Task
from app.services import get_tasks, add_task, update_task, delete_task
from app.database import tasks_db  # Importa a lista de tarefas

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bem vindo a API de tarefas!"}

@app.get("/tasks")
async def list_tasks():
    # Retorna todas as tarefas presentes na lista
    return tasks_db

@app.post("/tasks")
async def create_task(task: Task):
    return add_task(task)

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    task = get_tasks(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return task

@app.put("/tasks/{task_id}")
async def update_task_endpoint(task_id: int, task: Task):
    return update_task(task_id, task)

@app.delete("/tasks/{task_id}")
async def delete_task_endpoint(task_id: int):
    return delete_task(task_id)
