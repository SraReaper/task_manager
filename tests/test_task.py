import unittest
from app.models import Task

class TestTask(unittest.TestCase):
    def test_to_dict(self):
        task = Task(1, "Test Task")

        result = task.to_dict()

        expected = {
            "id": 1,
            "title": "Test Task",
            "completed": False
        }

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

