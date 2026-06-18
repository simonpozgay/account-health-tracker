from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum


class AccountStatus(Enum): 
    HEALTHY = 1
    BUYING = 2
    EXHAUSTED = 3
    DO_NOT_TOUCH = 4

class Account(BaseModel): 
    email: str
    platform: str
    status: AccountStatus


app = FastAPI()
next_id = 1

accounts: dict[int, Account] = {}

@app.get("/accounts")
def get_accounts(): 
    return accounts

@app.get("/accounts/{account_id}")
def get_account(account_id: int): 
    if account_id not in accounts: 
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts[account_id]

@app.post("/accounts")
def add_account(account: Account): 
    global next_id
    accounts[next_id] = account
    next_id += 1
    return account

@app.delete("/accounts/{account_id}")
def delete_account(account_id: int): 
    if account_id not in accounts: 
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts.pop(account_id)