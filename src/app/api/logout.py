from . import router

@router.get("/logout")
async def logout_user():
  # we'll create this function later
  # logout_user = await logout_user()
  return {"Status": "Logout Successful"}
