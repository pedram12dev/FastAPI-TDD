from .db_connection import Base
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)