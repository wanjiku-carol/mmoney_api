from . import router

@router.get("/transactions")
async def load_transactions():
  # we'll create this function later
  # transactions = await get_all_transactions()
  return {"Transactions": "List of transactions}
