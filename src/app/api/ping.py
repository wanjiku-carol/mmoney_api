from . import router

@router.get("/ping")
async def pong():
  return {"ping": "pong"}
