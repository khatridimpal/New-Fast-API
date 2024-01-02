from sqlalchemy import Boolean,Column,Integer,String
from database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer,primary_key=True,index=True)
    email = Column(String(100) , unique=True)
    username = Column(String(100))
    password = Column(String(100))
