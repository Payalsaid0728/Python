import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from app.schema.email_schema import EmailCreate

load_dotenv()

class EmailService:
    def __init__(self):
        pass 

    def send_email(self,email):
        if isinstance(email,dict):
            email=EmailCreate(**email)

        sender_email= os.getenv("EMAIL_ADDRESS")
        app_password=os.getenv("EMAIL_APP_PASSWORD")

        if not sender_email or not app_password:
            raise RuntimeError("EMAIL_ADDRESS or EMAIL_APP_PASSWORD is missing in .env")

        message = EmailMessage()
        message["subject"]=email.subject
        message["from"]=sender_email
        message["to"]=email.receiver_email
        message.set_content(email.body)

        with smtplib.SMTP("smtp.gmail.com",587,timeout=20) as server:
            server.starttls()
            server.login(sender_email,app_password)
            server.send_message(message)

    def send_reset_pin_email(self,receiver_email:str,pin:str):
        subject="Your Password Reset PIN"

        body=f"""
            Hello,
            You requested to reset your password.
            Your six-digit password reset PIN is:{pin}
            This pin expires in 5 minutes.
            If you did not request this,please ignore this email.

            Regards,
            Forgot Password Support
            """

        self.send_email(
            EmailCreate(receiver_email=receiver_email,subject=subject,body=body,)
        )

    def send_password_changed_email(self,receiver_email:str,new_password:str):
        subject="Password Changed Successfully"

        body=f"""
            Hello,
            Your password has been changed successfully.
            Your new password is :{new_password}
            If you did not make this change,please contact support.

            Regards,
            Forgot Password Support
            """
        
        self.send_email(
            EmailCreate(receiver_email=receiver_email,subject=subject,body=body,)
        )