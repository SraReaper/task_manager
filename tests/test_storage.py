import pytest
from app.models import Task
from app.storage import tasks, get_all_tasks

@pytest.fixture
def clean_storage():
    tasks.clear()

def test_get_all_tasks(clean_storage):

    # Create some test tasks
    task1 = Task(1, "Estudar Go")
    task2 = Task(2, "Estudar Python")

    # Add tasks to the storage
    tasks.append(task1)
    tasks.append(task2)

    # Retrieve all tasks using the get_all_tasks function
    result = get_all_tasks()

    # Assert that the retrieved tasks match the added tasks
    assert result == [task1, task2]
    
def test_get_all_tasks_empty(clean_storage):
        
        result = get_all_tasks()
        # Ensure the storage is empty
        assert result == []
        
def test_task_to_dict():
        task = Task(1, "Estudar Go")
        result = task.to_dict()
        assert result == {
                          "id": 1,
                          "title": "Estudar Go",
                          "completed": False
                          }