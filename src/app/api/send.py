from . import router

@router.get("/send")
async def send_money():
  # we'll create this function later
  # send_money = await send_money()
  return {"Amount": "10,000"}
