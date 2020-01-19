from . import router

@router.get("/signup")
async def signup_user():
  # we'll create this function later
  # create_user = await create_user()
  return {"Status": "User created Successfully"}
