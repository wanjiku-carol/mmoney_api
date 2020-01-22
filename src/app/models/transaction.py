from pydantic import BaseModel

class TransactionSchema(BaseModel):
  id: int
  u_id: int
  r_id: int
  amount: int
  money_type: str
  status: str
  created_at: datetime = None
