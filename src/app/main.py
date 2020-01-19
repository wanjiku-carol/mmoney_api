from fastapi import FastAPI
from app.api import (
  ping, send, countries, forgot_password, login, verify_sms,
  logout, recipients, signup, transactions, users, verify_email
)

app = FastAPI()

app.include_router(ping.router)
app.include_router(send.router)
app.include_router(countries.router)
app.include_router(forgot_password.router)
app.include_router(login.router)
app.include_router(verify_email.router)
app.include_router(logout.router)
app.include_router(recipients.router)
app.include_router(signup.router)
app.include_router(transactions.router)
app.include_router(users.router)
app.include_router(verify_email.router)
