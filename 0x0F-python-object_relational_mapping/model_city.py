#!/usr/bin/python3
""" city model """
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City table template """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
