from dataclass import dataclass

@dataclass
class EmailCreate:
    receiver_email:str
    subject:str
    body:str