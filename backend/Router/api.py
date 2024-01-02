from fastapi import FastAPI,Depends,status,HTTPException
from middleware.cors import add_cors_middleware
from dependencies.authentication import db_dependency
import Models.userModel as userModel
from schemas.LoginSchema import LoginBase
from schemas.RegisterSchema import RegisterBase
from config.database import engine
from utils.security import verify_password, get_password_hash
from sqlalchemy import select
from sqlalchemy.orm import Session



app = FastAPI()

add_cors_middleware(app)

userModel.Base.metadata.create_all(bind=engine)



@app.post("/token",status_code=status.HTTP_201_CREATED)
async def login(data: LoginBase,db: Session = db_dependency):
    query = select(userModel.User).where(userModel.User.email == data.email)
    user = db.execute(query).scalar()

    if user and verify_password(data.password ,user.password):
        return {"access_token": data.email, "token_type":"bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid creadentials",
        headers={"WWW-Authenticate":"Bearer"},
    )

@app.post("/register",status_code=status.HTTP_201_CREATED)
async def register(data: RegisterBase,db: Session = db_dependency):
    hashed_pass= get_password_hash(data.password)
    db_register =userModel.User(email=data.email, username =data.username,password =hashed_pass)
    db.add(db_register)
    db.commit()
    db.refresh(db_register)
    return {"user_id": db_register.user_id ,"email": db_register.email}
