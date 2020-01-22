from pydantic import BaseModel
from sqlalchemy.sql import func

class CountrySchema(BaseModel):
  id: int
  name: str
  created_at: datetime = None
