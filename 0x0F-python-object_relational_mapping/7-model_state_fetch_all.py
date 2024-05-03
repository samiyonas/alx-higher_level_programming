#!/usr/bin/python3
""" all states via sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3])
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    que = session.query(State).order_by(State.id).all()
    for i in que:
        print("{}: {}".format(i.id, i.name))
