from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Account(Base): 
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    platform = Column(String, nullable=False)

    purchases = relationship('Purchase', back_populates='account')
    
class Purchase(Base): 
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    account = Column(Integer, ForeignKey('accounts.id'))

    account = relationship('Account', back_populates='purchases')