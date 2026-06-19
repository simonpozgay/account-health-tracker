from pydantic import BaseModel
from datetime import date


class AccountCreate(BaseModel): 
    email: str
    platform: str

class AccountResponse(BaseModel): 
    id: int
    email: str
    platform: str
    last_purchase_date: date | None

    model_config = {"from_attributes": True}


class PurchaseCreate(BaseModel): 
    name: str
    quantity: int
    date: date
    account_id: int

class PurchaseResponse(BaseModel): 
    id: int
    name: str
    quantity: int
    date: date
    account_id: int

    model_config = {"from_attributes": True}