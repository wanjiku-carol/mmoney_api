from . import router

@router.get("/verify_sms")
async def verify_text():
  # we'll create this function later
  # sms_verification = await send_verify_sms()
  return {"Message": "Verification code 123456"}
