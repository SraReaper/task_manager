from app.models import Task
from app.storage import add_task, get_all_tasks as storage_get_all_tasks

next_id = 1


def create_task(title):

    global next_id
    task = Task(next_id, title)
    next_id += 1
    add_task(task)

    return task

def get_all_tasks():
    return storage_get_all_tasks()



