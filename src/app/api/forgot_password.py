from . import router

@router.get("/forgot_password")
async def forgot():
  # we'll create this function later
  # reset_password = await reset_password()
  return {"Status": "Reset Successful"}
