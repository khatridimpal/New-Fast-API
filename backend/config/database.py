from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE ='mysql+pymysql://root@localhost:3306/patient'

engine = create_engine(URL_DATABASE)
# engine = create_engine(URL_DATABASE, pool_pre_ping=True, pool_size=5, max_overflow=2, echo=True, client_encoding='utf8', encoding='utf-8')

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

Base = declarative_base()