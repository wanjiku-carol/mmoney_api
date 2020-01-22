import os

from databases import Database
from sqlalchemy import (
    create_engine, MetaData, Column, DateTime, Integer, String, Table,
    ForeignKey
    )
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine for communicating with the database
engine = create_engine(DATABASE_URL)

# metadata instance for creating the database schema
metadata = MetaData()

# create tables
user = Table(
  "user",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(50)),
  Column("email", String(200), unique=True),
  Column("dob", DateTime),
  Column("bank_code", Integer),
  Column("mobile", Integer, nullable=False),
  Column("password", String(100)),
  Column("pin", String(100)),
  Column("created_date", DateTime, default=func.now(), nullable=False),
)
recipient = Table(
  "recipient",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(50)),
  Column("money_type", String(50)),
  Column("mobile", Integer),
  Column("bank_code", Integer),
  Column("created_date", DateTime, default=func.now(), nullable=False),
)
country = Table(
  "country",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(50)),
  Column("created_date", DateTime, default=func.now(), nullable=False),
)
transaction = Table(
  "transaction",
  metadata,
  Column('id', Integer, primary_key=True),
  Column('u_id', Integer, ForeignKey("user.id")),
  Column('r_id', Integer, ForeignKey("recipient.id")),
  Column('amount', Integer),
  Column('status', String(50)),
  Column('created_at', DateTime, default=func.now(), nullable=False),
  )

# new database instance. Databases is an async SQL query builder that
# works on top of the SQLAlchemy Core expression language

database = Database(DATABASE_URL)
