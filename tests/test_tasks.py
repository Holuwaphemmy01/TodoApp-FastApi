import unittest
from fastapi.testclient import TestClient
from src.main import app

# Create a test client
client = TestClient(app)

class TestFastAPI(unittest.TestCase):

    def test_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_hello_name(self):
        response = client.get("/hello/John")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello John"})

    def test_tasks_list(self):
        response = client.get("/api/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == "__main__":
    unittest.main()