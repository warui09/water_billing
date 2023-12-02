#!/usr/bin/python3
"""User class"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    meter_number = Column(Integer, nullable=False)
    phone_number = Column(String(13), nullable=False)
    address = Column(String(50), nullable=False)
