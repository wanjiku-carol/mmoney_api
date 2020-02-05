import json
import pytest

from app.api import users

def test_get_users(test_app, monkeypatch):
  test_data = [
    {
    "id": 1,
    "name": "Jane Wanjiku",
    "email": "jane@emailt.com",
    "dob": "08-11-2017",
    "password": "password",
    "pin": "1234",
    "money_type": "mobile",
    "mobile": "0703123456",
    "bank_code": "097-123456",
  },
  {
    "id": 2,
    "name": "Stephen Odom",
    "email": "steve@emailt.com",
    "dob": "08-11-2017",
    "password": "password",
    "pin": "1234",
    "money_type": "mobile",
    "mobile": "0766123456",
    "bank_code": "097-12345690",
  }
  ]

  async def mock_get_all():
    return test_data
  
  monkeypatch.setattr(users, "get_all", mock_get_all)

  response = test_app.get("/users")
  assert response.status_code == 200
  assert response.json() == test_data

def test_invalid_get_users(test_app, monkeypatch):
  async def mock_get_all():
    return None

  monkeypatch.setattr(users, "get_all", mock_get_all)

  response = test_app.get("/users")
  assert response.status_code == 404
  assert response.json()["detail"] == "No Users Found"

def test_get_user(test_app, monkeypatch):
  test_user = {
    "id": 1,
    "name": "Jane Wanjiku",
    "email": "jane@emailt.com",
    "dob": "08-11-2017",
    "password": "password",
    "pin": "1234",
    "money_type": "mobile",
    "mobile": "0703123456",
    "bank_code": "097-123456",
  }
  async def mock_get(id):
    return test_user
  
  monkeypatch.setattr(users, "get", mock_get)

  response = test_app.get("/users/1")
  assert response.status_code == 200
  assert response.json() == test_user

def test_invalid_get_user(test_app, monkeypatch):
  async def mock_get(id):
    return None

  monkeypatch.setattr(users, "get", mock_get)

  response = test_app.get("/users/999")
  assert response.status_code == 404
  assert response.json()['detail'] == "User Not Found"

def test_create_users(test_app, monkeypatch):
  test_user_payload = {
    "name": "Jane Wanjiku",
    "email": "jane@emailt.com",
    "dob": "08-11-2017",
    "password": "password",
    "pin": "1234",
    "money_type": "mobile",
    "mobile": "0703123456",
    "bank_code": "097-123456"
  }
  test_user_response = {
    "success": "Account Successfully Created",
  }

  async def mock_post(payload):
    return 1

  monkeypatch.setattr(users, "post", mock_post)

  response = test_app.post("/users", data=json.dumps(test_user_payload),)
  assert response.status_code == 201
  assert response.json() == test_user_response

def test_invalid_create_users(test_app):
  response = test_app.post("/users", data=json.dumps({"fake": "fake data"}))
  assert response.status_code == 422

  test_data = {
    "name": "Jane Wanjiku",
    "email": "",
    "dob": "08-11-2017",
    "password": "password",
    "pin": "1234",
    "money_type": "mobile",
    "mobile": "0703123456",
    "bank_code": "097-123456"
  }

  response = test_app.post("/users", data=json.dumps(test_data))
  assert response.status_code == 422


def test_update_user(test_app, monkeypatch):
  pass

def test_invalid_update_user(test_app, monkeypatch):
  pass

def test_detete_user(test_app, monkeypatch):
  pass

def test_invalid_delete_user(test_app, monkeypatch):
  pass


