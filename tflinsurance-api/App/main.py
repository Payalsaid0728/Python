from fastapi import FastAPI

from App.api.routes.policy_routes import router as policy_router
from App.repositories.policy_repository import PolicyRepository
from App.services.policy_service import PolicyService

App = FastAPI(title="TFLInsurance API",description="Insurance Policy Management REST API",version="1.0")

# Create shared application dependencies
repository = PolicyRepository()

App.state.policy_service = PolicyService(repository)

# Register API routes
App.include_router(policy_router)


@App.get("/")
def home():
    return {
        "application": "TFLInsurance",
        "message": "Welcome to TFLInsurance REST API",
        "docs": "/docs"
    }