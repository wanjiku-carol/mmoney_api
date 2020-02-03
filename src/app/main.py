from fastapi import FastAPI

from app.api import (
  ping, send, countries, forgot_password, login, verify_sms,
  logout, recipients, signup, transactions, users, verify_email
)
from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
  await database.connect()

@app.on_event("shutdown")
async def shutdown():
  await database.disconnect()

app.include_router(ping.router)
app.include_router(send.router)
app.include_router(countries.router, prefix='/countries', tags=['countries'])
app.include_router(forgot_password.router)
app.include_router(login.router)
app.include_router(verify_email.router)
app.include_router(logout.router)
app.include_router(recipients.router)
app.include_router(signup.router)
app.include_router(transactions.router)
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(verify_email.router)
