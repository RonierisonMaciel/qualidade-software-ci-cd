from app.services import get_tasks, add_task, update_task, delete_task
from app.models import Task
from app.database import tasks_db
import pytest

# (Opcional) Fixture para limpar o "banco de dados" em memória antes de cada teste
@pytest.fixture(autouse=True)
def clear_db():
    tasks_db.clear()

def test_add_task():
    """
    Testa se a função add_task insere corretamente uma tarefa.
    """
    task = Task(id=1, title="Title Task", description="Task Description", status=False)
    result = add_task(task)
    assert result == task
    # Verifica se a tarefa está no "banco de dados"
    assert get_tasks(1) == task

def test_get_task():
    """
    Testa se a função get_tasks retorna a tarefa correta pelo ID.
    """
    # Primeiro adiciona a tarefa
    task = Task(id=2, title="Another Task", description="Another Description", status=False)
    add_task(task)

    # Em seguida, busca a tarefa
    fetched_task = get_tasks(2)
    assert fetched_task == task

def test_update_task():
    """
    Testa se a função update_task atualiza corretamente a tarefa.
    """
    # Cria a tarefa inicial
    original_task = Task(id=3, title="Original Task", description="Original Description", status=False)
    add_task(original_task)

    # Define uma versão atualizada
    updated_task = Task(id=3, title="Updated Task", description="Updated Description", status=True)

    # Chama a função de atualização
    result = update_task(3, updated_task)
    assert result == updated_task

    # Verifica se a tarefa foi realmente atualizada
    assert get_tasks(3) == updated_task

def test_delete_task():
    """
    Testa se a função delete_task deleta corretamente a tarefa.
    """
    # Cria a tarefa para depois deletar
    task = Task(id=4, title="Task to Delete", description="Delete Me", status=False)
    add_task(task)

    # Deleta e checa a resposta
    response = delete_task(4)
    assert response == {"message": "Task deletada com sucesso!"}

    # Verifica se a tarefa foi removida
    assert get_tasks(4) is None
