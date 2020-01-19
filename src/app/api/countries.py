from . import router

@router.get("/countries")
async def load_countries():
  # we'll create this function later
  # countries = await get_all_countries()
  return {"Country": "Kenya"}
