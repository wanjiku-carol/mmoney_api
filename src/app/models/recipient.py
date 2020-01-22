from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from . import Base

class Recipient(Base):
  __tablename__ = "recipients"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(200))
  money_type = Column(String(100))
  mobile = Column(Integer)
  bank_code = Column(Integer)
  created_at = Column(DateTime, default=func.now(), nullable=False)
