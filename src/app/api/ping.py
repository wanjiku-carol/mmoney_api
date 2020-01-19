from . import router

@router.get("/ping")
def pong():
  return {"ping": "pong"}
