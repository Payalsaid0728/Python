from fastapi import FastAPI
from app.api.routes.email_routes import router as email_router
from app.services.email_service import EmailService

app=FastAPI(title="forgot Password API",description="Password reset using FastAPI,MySQL and Gmail",version="1.0.0")

app.state.email_service = EmailService()


# Register API routes
app.include_router(email_router)
@app.get("/")
def home():
    return{
        "application":"Email API",
        "message":"Welcome to Email REST API",
        "docs":"/docs"
    }