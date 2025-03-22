import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker


DEV_DATABASE_URL = os.getenv('DEV_DATABASE_URL')
engine = create_engine(DEV_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=True)
Base = declarative_base()

def db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
