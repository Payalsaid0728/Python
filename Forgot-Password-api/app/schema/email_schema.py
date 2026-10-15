from pydantic import BaseModel,Field

class EmailCreate(BaseModel):
    receiver_email:str=Field(min_length=2,max_length=100)
    subject:str=Field(min_length=2,max_length=100)
    body:str=Field(min_length=2,max_length=100)