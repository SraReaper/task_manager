class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.completed = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

#Testing the Task class
task1 = Task(1, "First Task")

print(task1.id)
print(task1.title)
print(task1.completed)