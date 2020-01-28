from . import router
from app.models.country import CountrySchema, CountryDB
from app.db import country, database
from sqlalchemy import select
from fastapi import HTTPException
from typing import List

# get all countries
async def get_all():
  query = country.select().order_by(country.c.id)
  return await database.fetch_all(query=query)

@router.get("/countries", response_model=List[CountryDB])
async def get_countries():
  return await get_all()

# get one country
async def get(id: int):
  query = country.select().where(id == country.c.id)
  return await database.fetch_one(query=query)

@router.get("/countries/{id}", response_model=CountryDB, status_code=200)
async def get_country(id: int):
  country = await get(id)
  if not country:
    raise HTTPException(status_code=404, detail="Country Not Found")
  return country

# post request
async def post(payload: CountrySchema):
  query = country.insert().values(name=payload.name)
  return await database.execute(query=query)


@router.post("/countries", response_model=CountryDB, status_code=201)
async def create_country(payload: CountrySchema):
  country_id = await post(payload)
  response_object = {
    "id": country_id,
    "name": payload.name,
    }
  return response_object
