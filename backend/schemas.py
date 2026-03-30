from pydantic import BaseModel

class TransactionCreate(BaseModel):
    date: str
    amount: float
    type: str
    category: str
    note: str
