from app.models import Task

next_id = 1
tasks = []

def create_task(title):
    global next_id

    task = Task(id=next_id, title=title)
    
    next_id += 1

    tasks.append(task)

    return task



