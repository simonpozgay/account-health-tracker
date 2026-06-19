from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, Account
from schemas import AccountCreate, AccountResponse


app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/accounts", response_model=list[AccountResponse])
def get_accounts(db: Session = Depends(get_db)): 
    return db.query(Account).all()

@app.get("/accounts/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)): 
    query = db.query(Account).filter(Account.id == account_id).one_or_none()
    
    if query is None: 
        raise HTTPException(status_code=404, detail="Account not found")
    return query

@app.post("/accounts", response_model=AccountResponse)
def add_account(account: AccountCreate, db: Session = Depends(get_db)): 
    db_account = Account(email=account.email, platform=account.platform)

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account

@app.delete("/accounts/{account_id}", response_model=AccountResponse)
def delete_account(account_id: int, db: Session = Depends(get_db)): 
    target = db.query(Account).filter(Account.id == account_id).one_or_none()
    
    if target is None: 
        raise HTTPException(status_code=404, detail="Account not found")

    db.delete(target)
    db.commit()
    return target