from . import router

@router.get("/login")
async def login_user():
  # we'll create this function later
  # login_user = await login_user()
  return {"Status": "Login Successful"}
