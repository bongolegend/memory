import pytest
from google.cloud import firestore
from unittest import mock
from memory.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def firestore_client_mock():
    with mock.patch('memory.app.db', autospec=True) as mock_client:
        yield mock_client

def test_create_user(client):
    response = client.post('/users', json={'name': 'John Doe'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'John Doe'

def test_get_user(client, firestore_client_mock):
    firestore_client_mock().collection().document().get().to_dict.return_value = {
        'id': 'user-1234',
        'name': 'John Doe',
        'created_at': firestore.SERVER_TIMESTAMP
    }
    response = client.get('/users/user-1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 'user-1234'
    assert data['name'] == 'John Doe'

def test_update_user(client):
    response = client.put('/users/user-1234', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']

def test_delete_user(client):
    response = client.delete('/users/user-1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']

def test_create_journal(client):
    response = client.post('/users/user-1234/journals', json={'name': 'My Journal'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'My Journal'

def test_get_journal(client, firestore_client_mock):
    firestore_client_mock().collection().document().collection().document().get().to_dict.return_value = {
        'id': 'jour-1234',
        'name': 'My Journal',
        'created_at': firestore.SERVER_TIMESTAMP
    }
    response = client.get('/users/user-1234/journals/jour-1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 'jour-1234'
    assert data['name'] == 'My Journal'

def test_update_journal(client):
    response = client.put('/users/user-1234/journals/jour-1234', json={'name': 'Updated Journal'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']

def test_delete_journal(client):
    response = client.delete('/users/user-1234/journals/jour-1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']

def test_create_entry(client):
    response = client.post('/users/user-1234/journals/jour-1234/entries', json={
        'name': 'First Entry',
        'content': 'This is the content of the first entry.'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'First Entry'
    assert data['content'] == 'This is the content of the first entry.'

def test_get_entry(client, firestore_client_mock):
    firestore_client_mock().collection().document().collection().document().collection().document().get().to_dict.return_value = {
        'id': 'entr-1234',
        'name': 'First Entry',
        'content': 'This is the content of the first entry.',
        'created_at': firestore.SERVER_TIMESTAMP
    }
    response = client.get('/users/user-1234/journals/jour-1234/entries/entr-1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 'entr-1234'
    assert data['name'] == 'First Entry'
    assert data['content'] == 'This is the content of the first entry.'

def test_update_entry(client):
    response = client.put('/users/user-1234/journals/jour-1234/entries/entr-1234', json={
        'name': 'Updated Entry',
        'content': 'Updated content.'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']

def test_delete_entry(client):
    response = client.delete('/users/user-1234/journals/jour-1234/entries/entr-1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']
