from . import router

@router.get("/verify_email")
async def verify_email_address():
  # we'll create this function later
  # email_verification = await send_verify_email()
  return {"Message": "Verification link: http://bitly/activate"}
