from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSchema(BaseModel):
  name: str
  email: EmailStr
  dob: str
  password: str
  pin: str
  money_type: str = None
  mobile : str
  bank_code: str = None

class UserDB(UserSchema):
  id: int
  
class UserSchemaOut(BaseModel):
  id: int
  name: str
  email: EmailStr
  dob: str
  money_type: str = None
  mobile : str
  bank_code: str = None

class UserSchemaUpdate(BaseModel):
  name: str = None
  email: EmailStr = None
  dob: str = None
  money_type: str = None
  mobile : str = None
  bank_code: str = None
