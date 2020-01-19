from . import router

@router.get("/users")
async def load_users():
  # we'll create this function later
  # users = await get_all_users()
  return {"Users": "List of users"}
