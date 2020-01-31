from pydantic import BaseModel, Field
from sqlalchemy.sql import func

class CountrySchema(BaseModel):
  name: str = Field(..., min_length=3, max_length=74)

class CountryDB(CountrySchema):
  id: int
