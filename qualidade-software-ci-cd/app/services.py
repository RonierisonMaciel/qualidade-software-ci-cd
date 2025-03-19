# app/services.py

from fastapi import HTTPException
from app.database import tasks_db
from app.models import Task

def get_tasks(task_id: int):
    """Busca e retorna a task cujo id é igual a task_id, ou None se não encontrada."""
    return next((task for task in tasks_db if task.id == task_id), None)

def add_task(task: Task):
    """Adiciona uma nova task à lista."""
    tasks_db.append(task)
    return task

def update_task(task_id: int, updated_task: Task):
    """Atualiza uma task existente. Lança exceção se não encontrada."""
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task não encontrada")

def delete_task(task_id: int):
    """Remove uma task com o id especificado."""
    global tasks_db
    tasks_db = [task for task in tasks_db if task.id != task_id]
    return {"message": "Task deletada com sucesso!"}
