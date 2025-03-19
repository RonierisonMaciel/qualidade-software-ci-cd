from app.services import get_tasks, add_task, update_task, delete_task
from app.models import Task

def test_add_task():
    task = Task(id=1, title="Title Task", description="Task Description", status=False)
    assert add_task(task) == task

def test_get_task():
    assert get_tasks(1)

def test_update_task():
    update_tasks = Task(id=1, title="Title Task", description="Task Description", status=True)
    assert update_task(1, update_tasks) == update_tasks

def test_delete_task():
    assert delete_task(1) == {"message": "Task deletada com sucesso!"}