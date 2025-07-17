# import pytest
# from httpx import AsyncClient
# from src.db_utils import collection
#
# # Use async client
# client = AsyncClient(base_url="http://test")
#
#
# # Clean database before and after tests
# @pytest.fixture(autouse=True)
# async def clear_database():
#     await collection.delete_many({})
#     yield
#
# # ----------------------------
# # Test Cases
# # ----------------------------
#
# @pytest.mark.asyncio
# def test_create_task():
#     print("Code reaches here 1")
#     async with AsyncClient(base_url="http://test") as client:
#         response =  client.post("/api/tasks", json={"title": "Test Task"})
#         print(response.json())
#         print("Code reaches here")
#         assert response.status_code == 201
#         data = response.json()
#         assert data["title"] == "Test Task"
#         assert data["completed"] is False
#         assert "id" in data
#
#
# # @pytest.mark.asyncio
# # async def test_get_all_tasks():
# #     # Create two tasks
# #     await client.post("/api/tasks", json={"title": "Task 1"})
# #     await client.post("/api/tasks", json={"title": "Task 2"})
# #
# #     response = await client.get("/api/tasks")
# #     assert response.status_code == 200
# #     tasks = response.json()
# #     assert isinstance(tasks, list)
# #     assert len(tasks) == 2
# #
# #
# # @pytest.mark.asyncio
# # async def test_get_single_task():
# #     create_resp = await client.post("/api/tasks", json={"title": "Single Task"})
# #     task_id = create_resp.json()["id"]
# #
# #     response = await client.get(f"/api/tasks/{task_id}")
# #     assert response.status_code == 200
# #     data = response.json()
# #     assert data["id"] == task_id
# #     assert data["title"] == "Single Task"
# #
# #
# # @pytest.mark.asyncio
# # async def test_update_task():
# #     create_resp = await client.post("/api/tasks", json={"title": "Old Title"})
# #     task_id = create_resp.json()["id"]
# #
# #     update_data = {"title": "New Title", "completed": True}
# #     response = await client.put(f"/api/tasks/{task_id}", json=update_data)
# #     assert response.status_code == 200
# #     updated = response.json()
# #     assert updated["title"] == "New Title"
# #     assert updated["completed"] is True
# #
# #
# # @pytest.mark.asyncio
# # async def test_delete_task():
# #     create_resp = await client.post("/api/tasks", json={"title": "To Delete"})
# #     task_id = create_resp.json()["id"]
# #
# #     delete_response = await client.delete(f"/api/tasks/{task_id}")
# #     assert delete_response.status_code == 204
# #
# #     get_response = await client.get(f"/api/tasks/{task_id}")
# #     assert get_response.status_code == 404
# #
# #
# # @pytest.mark.asyncio
# # async def test_get_nonexistent_task():
# #     response = await client.get("/api/tasks/this-is-not-a-real-id")
# #     assert response.status_code == 404



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