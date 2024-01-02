from fastapi import Depends
from config.database import SessionLocal

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


# db_dependency = Union[Session,Depends(get_db)]

db_dependency =Depends(get_db)
