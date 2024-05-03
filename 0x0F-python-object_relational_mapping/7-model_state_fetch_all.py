#!/usr/bin/python3
""" all states via sqlalchemy """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(State).order_by(State.id)
for i in query:
    print("{}: {}".format(i.id, i.name))
