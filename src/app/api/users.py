from datetime import datetime
from fastapi import HTTPException
from . import router
from app.models.user import UserSchema, UserDB
from app.db import user, database
from typing import List

@router.get("/users")
async def get_users():
  # we'll create this function later
  # users = await get_all_users()
  return {"Users": "List of users"}

async def post(payload: UserSchema):
  query = user.insert().values(
    name=payload.name,
    email=payload.email,
    dob=datetime.strptime(payload.dob, '%d-%b-%Y'),
    password=payload.password,
    pin=payload.pin,
    money_type=payload.money_type,
    mobile=payload.mobile,
    bank_code=payload.bank_code,
    )
  return await database.execute(query=query)

@router.post("/users", status_code=201)
async def create_user(payload: UserSchema):
  user_id = await post(payload)
  
  response_object = {
    "success": "Account Successfully Created",
    }
  return response_object

async def get(id: int):
  query = user.select().where(id == user.c.id)
  return await database.fetch_one(query=query)

@router.get("/users/{id}", response_model=UserDB, status_code=200)
async def get_user(id: int):
  user = await get(id)

  if not user:
    raise HTTPException(status_code=404, detail="User Not Found")
  return user

