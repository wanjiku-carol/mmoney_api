from pyndatic import BaseModel

class User(BaseModel):

  id: int
  name: str
  email: str
  dob: dateime = None
  password: str
  pin: str
  money_type: str
  mobile : int
  bank_code: int
  created_at: dateime = None
