from app.services import create_task


def test_create_task():
    task = create_task("Estudar Python")

    assert task.id == 1
    assert task.title == "Estudar Python"
    assert task.completed is False
    