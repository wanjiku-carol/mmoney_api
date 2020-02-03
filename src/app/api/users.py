from datetime import datetime
from fastapi import Body
from . import router
from app.models.user import UserSchema, UserDB
from app.db import user, database


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
