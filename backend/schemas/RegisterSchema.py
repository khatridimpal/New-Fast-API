from pydantic import BaseModel

class RegisterBase(BaseModel):
    email :str
    username : str
    password :str