# models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = "brands"  # Table name in MySQL

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(255))
    about = Column(Text)
    privacy_policy = Column(Text)
    return_policy = Column(Text)
