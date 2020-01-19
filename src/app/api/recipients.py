from . import router

@router.get("/recipients")
async def load_recipients():
  # we'll create this function later
  # recipients = await get_all_recipients()
  return {"Recipients": "List of recipients"}
