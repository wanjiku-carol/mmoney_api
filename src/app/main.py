from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def pong():
  return {"ping": "pong"}

@app.get("/balance")
async def balancer():
  # we'll create this function later
  # balances = await get_all_balances()
  return {"Balance": "10,000"}
