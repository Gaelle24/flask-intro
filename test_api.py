import pytest
from unittest.mock import patch
from routes import app, connect_db  

@pytest.fixture
def client():
    """Sets up an isolated database for clean unit testing"""
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'test_flasktask.db'

    with app.test_client() as client:
        db = connect_db()
        db.execute('DROP TABLE IF EXISTS ftasks')
        db.execute('''
            CREATE TABLE ftasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                due_date TEXT,
                priority INTEGER,
                status INTEGER
            )
        ''')
        db.commit()
        db.close()
        yield client

# Positive Cases
def test_api_get_tasks_empty(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'success'

def test_api_create_task_success(client):
    response = client.post('/api/tasks', json={"name": "Finish Drill", "due_date": "06/15", "priority": 5})
    assert response.status_code == 201

def test_api_get_tasks_with_data(client):
    client.post('/api/tasks', json={"name": "Review Code"})
    response = client.get('/api/tasks')
    assert len(response.get_json()['tasks']) == 1

def test_api_update_task_success(client):
    client.post('/api/tasks', json={"name": "Old"})
    response = client.put('/api/tasks/1', json={"name": "New", "due_date": "07/01", "priority": 2})
    assert response.status_code == 200

def test_api_delete_task_success(client):
    client.post('/api/tasks', json={"name": "Delete Me"})
    response = client.delete('/api/tasks/1')
    assert response.status_code == 200

#Negative Cases
def test_api_create_task_missing_name(client):
    response = client.post('/api/tasks', json={"due_date": "06/15"})
    assert response.status_code == 400

def test_api_create_task_non_json(client):
    response = client.post('/api/tasks', data="Not JSON String")
    assert response.status_code == 400

def test_api_update_task_not_found(client):
    response = client.put('/api/tasks/999', json={"name": "Ghost"})
    assert response.status_code == 404

def test_api_update_task_non_json(client):
    response = client.put('/api/tasks/1', data="Not JSON")
    assert response.status_code == 400

def test_api_delete_task_not_found(client):
    response = client.delete('/api/tasks/999')
    assert response.status_code == 404


@patch('api.connect_db')
def test_api_get_tasks_database_crash(mock_connect, client):
    """Forces the database to crash during a GET request"""
    mock_connect.side_effect = Exception("Database connection failed")
    response = client.get('/api/tasks')
    assert response.status_code == 500
    assert response.get_json()['status'] == 'error'

@patch('api.connect_db')
def test_api_create_task_database_crash(mock_connect, client):
    """Forces the database to crash during a POST request"""
    mock_connect.side_effect = Exception("Database write failed")
    response = client.post('/api/tasks', json={"name": "Crash Test"})
    assert response.status_code == 500
    assert response.get_json()['status'] == 'error'

@patch('api.connect_db')
def test_api_update_task_database_crash(mock_connect, client):
    """Forces the database to crash during a PUT request"""
    mock_connect.side_effect = Exception("Database update failed")
    response = client.put('/api/tasks/1', json={"name": "Crash Test"})
    assert response.status_code == 500
    assert response.get_json()['status'] == 'error'

@patch('api.connect_db')
def test_api_delete_task_database_crash(mock_connect, client):
    """Forces the database to crash during a DELETE request"""
    mock_connect.side_effect = Exception("Database delete failed")
    response = client.delete('/api/tasks/1')
    assert response.status_code == 500
    assert response.get_json()['status'] == 'error'