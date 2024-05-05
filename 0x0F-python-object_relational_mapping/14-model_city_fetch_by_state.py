#!/usr/bin/python3
""" model city fetch by state """
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3])
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    que = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    for i, j in que:
        print("{}: ({}) {}".format(j.name, i.id, i.name))
