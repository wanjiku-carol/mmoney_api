from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSchema(BaseModel):
  name: str
  email: EmailStr
  dob: str = None
  password: str
  pin: str
  money_type: str
  mobile : str
  bank_code: str = None

class UserDB(UserSchema):
  id: int
  