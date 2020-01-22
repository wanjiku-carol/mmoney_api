from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from . import Base

class Country(Base):
  __tablename__ = "countries"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100))
  created_at = Column(DateTime, default=func.now(), nullable=False)
