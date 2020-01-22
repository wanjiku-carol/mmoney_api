from pydantic import BaseModel

from . import Base

class RecipientSchema(BaseModel):

  id: int
  name: str
  money_type: int
  mobile; int
  bank_code: int
  created_at: datetime = None
