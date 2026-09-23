from app.services import create_task
from app.services import update_title_task


def test_create_task():
    task = create_task("Estudar Python")

    assert task.id == 1
    assert task.title == "Estudar Python"
    assert task.completed is False
    
def test_update_title_task_not_found():
    result = update_title_task(56, "Estudar Java")

    assert result is None
    