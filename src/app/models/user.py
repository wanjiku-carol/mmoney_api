# from sqlalchemy import Boolean, Column, Integer, String, DateTime
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# from . import Base

# class User(Base):
#   __tablename__ = "users"

#   id = Column(Integer, primary_key=True, index=True)
#   name = Column(String(200))
#   email = Column(String(200))
#   dob = Column(DateTime)
#   password = Column(String(100))
#   pin = Column(String(100))
#   money_type = Column(String(100))
#   mobile = Column(Integer)
#   bank_code = Column(Integer)
#   created_at = Column(DateTime, default=func.now(), nullable=False)
