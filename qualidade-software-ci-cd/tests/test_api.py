# tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app
from app.database import tasks_db

client = TestClient(app)

def test_create_task():
    tasks_db.clear()  # Limpa o "banco" para garantir teste independente
    response = client.post("/tasks", json={
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    }

def test_list_tasks():
    tasks_db.clear()
    # Cria uma task para testar listagem
    client.post("/tasks", json={
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    })
    response = client.get("/tasks")
    assert response.status_code == 200
    # Verifica se retorna uma lista com 1 item
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1

def test_read_task():
    tasks_db.clear()
    # Cria uma task para testar leitura
    client.post("/tasks", json={
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    })
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    }

def test_update_task():
    tasks_db.clear()
    # Cria uma task para testar atualização
    client.post("/tasks", json={
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    })
    response = client.put("/tasks/1", json={
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": True
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": True
    }

def test_delete_task():
    tasks_db.clear()
    # Cria uma task para testar deleção
    client.post("/tasks", json={
        "id": 1,
        "title": "Title Task",
        "description": "Task Description",
        "status": False
    })
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deletada com sucesso!"}