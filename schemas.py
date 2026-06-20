from pydantic import BaseModel
from datetime import date


class AccountCreate(BaseModel): 
    email: str
    platform: str

class AccountUpdate(BaseModel): 
    email: str | None
    platform: str | None

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

class PurchaseUpdate(BaseModel): 
    name: str | None
    quantity: int | None
    date: date | None
    account_id = int | None

class PurchaseResponse(BaseModel): 
    id: int
    name: str
    quantity: int
    date: date
    account_id: int

    model_config = {"from_attributes": True}