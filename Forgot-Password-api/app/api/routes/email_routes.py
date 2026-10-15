from fastapi import APIRouter,HTTPException,Request
from app.schema.email_schema import EmailCreate

router=APIRouter(
    prefix="/api/email",
    tags=["emails"],
)

@router.post("/send")
def send_email(email:EmailCreate,request:Request):
    try:
        service=request.app.state.email_service
        service.send_email(email)
        return{"message":"email has been successfully sent"}
    except Exception as exc:
        raise HTTPException(status_code=500,detail=str(exc)) from exc