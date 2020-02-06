from datetime import datetime
from fastapi import HTTPException
from . import router
from app.models.user import UserSchema, UserDB, UserSchemaOut, UserSchemaUpdate
from app.db import user, database
from typing import List


async def post(payload: UserSchema):
  payload.dict()["dob"] = datetime.strptime(payload.dob, '%d-%b-%Y')
  query = user.insert(), [payload.dict()]
  return await database.execute(query=query)

@router.post("/users", response_model=UserSchemaOut, status_code=201)
async def create_user(payload: UserSchema):
  user_id = await post(payload)

  response_object = {
    "id": user_id,
    "name": payload.name,
    "email": payload.email,
    "dob": payload.dob,
    "money_type": payload.money_type,
    "mobile": payload.mobile,
    "bank_code": payload.bank_code
    }
  return response_object

async def get(id: int):
  query = user.select().where(id == user.c.id)
  return await database.fetch_one(query=query)

@router.get("/users/{id}", response_model=UserDB, status_code=200)
async def get_user(id: int):
  user_id = await get(id)

  if not user_id:
    raise HTTPException(status_code=404, detail="User Not Found")
  return user_id

async def get_all():
  query = user.select().order_by(user.c.name)
  return await database.fetch_all(query=query)

@router.get("/users", response_model=List[UserDB], status_code=200)
async def get_users():
  countries = await get_all()
  if not countries:
    raise HTTPException(status_code=404, detail="No Users Found")
  return countries

async def put(id: int, payload: UserSchemaUpdate):
  query = (
    user
    .update(payload.dict())
    .where(id == user.c.id)
    .returning(user.c.id)
    )
  return await database.execute(query=query)


@router.put("/users/{id}", status_code=201)
async def update_user(payload: UserSchemaUpdate, id: int):
  user_id = await get(id)
  if not user_id:
    raise HTTPException(status_code=404, detail="User Not Found")
  
  user_update = await put(id, payload)

  # get_again = await get(id)
  response_object = {}
  for k,v in payload.dict().items():
    if v is not None:
      response_object[k] = v
  response_object["id"] = user_update
  return response_object
