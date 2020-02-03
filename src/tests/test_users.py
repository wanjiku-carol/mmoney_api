import json
import pytest

from app.api import users

def test_get_users(test_app, monkeypatch):
  pass
  # test_user_data = [{
    # "name": "",
    # "email": "",
    # "dob": "",
    # "mobile"; "",
    # "bank_code": "",
    # "created_at": ""
  # }]

def test_invalid_get_users(test_app, monkeypatch):
  pass

def test_get_user(test_app, monkeypatch):
  pass

def test_invalid_get_user(test_app, monkeypatch):
  pass

def test_create_users(test_app, monkeypatch):
  test_user_payload = {
    "name": "Jane Wanjiku",
    "email": "jane@emailt.com",
    "dob": "08-11-2017",
    "password": "password",
    "pin": "1234",
    "money_type": "mobile",
    "mobile": "0703123456",
    "bank_code": "097-123456",
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

def test_invalid_create_users(test_app, monkeypatch):
  pass

def test_update_user(test_app, monkeypatch):
  pass

def test_invalid_update_user(test_app, monkeypatch):
  pass

def test_detete_user(test_app, monkeypatch):
  pass

def test_invalid_delete_user(test_app, monkeypatch):
  pass


