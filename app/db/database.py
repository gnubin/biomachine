import os
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = f"{os.getenv('DB_URL')}" 

class Base(DeclarativeBase): 
           pass


engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False, 
)
