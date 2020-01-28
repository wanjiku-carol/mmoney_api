from pydantic import BaseModel
from sqlalchemy.sql import func

class CountrySchema(BaseModel):
  name: str

class CountryDB(CountrySchema):
  id: int
