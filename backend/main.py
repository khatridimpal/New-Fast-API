from fastapi import FastAPI,Depends,status,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import model
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import uvicorn
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the actual origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterBase(BaseModel):
    email :str
    username : str
    password :str

class LoginBase(BaseModel):
    email :str
    password:str

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


# db_dependency = Union[Session,Depends(get_db)]

db_dependency =Depends(get_db)


@app.post("/token",status_code=status.HTTP_201_CREATED)
async def login(data: LoginBase,db: Session = db_dependency):
    query = select(model.User).where(model.User.email == data.email)
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
    db_register =model.User(email=data.email, username =data.username,password =hashed_pass)
    db.add(db_register)
    db.commit()
    db.refresh(db_register)
    return {"user_id": db_register.user_id ,"email": db_register.email}

# security = OAuth2PasswordBearer(tokenUrl="token")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)

if __name__ == "__main__":
    uvicorn.run(app ,host="127.0.0.1" , port=8080)