import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task

@pytest.fixture
def user(db):
    return User.objects.create_user(username='postgres', password='root')

@pytest.fixture
def authenticated_client(client, user):
    client.login(username='postgres', password='root')
    return client

@pytest.fixture
def task(user):
    return Task.objects.create(
        title='Test Task',
        description='Test Task Description',
        status='Pending',
        due_date='2025-05-01',
        user=user
    )

def test_task_create(authenticated_client, user):
    task_data = {
        'title': 'New Task',
        'description': 'Description of new task',
        'status': 'Pending',
        'due_date': '2025-05-02'
    }
    response = authenticated_client.post(reverse('task_create'), task_data)
    assert response.status_code == 302
    assert Task.objects.filter(title='New Task', user=user).exists()

def test_task_list(authenticated_client, task):
    response = authenticated_client.get(reverse('task_list'))
    assert response.status_code == 200
    assert b'Test Task' in response.content
