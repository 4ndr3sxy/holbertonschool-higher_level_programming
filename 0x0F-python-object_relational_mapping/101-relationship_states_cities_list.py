#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    query_inner = session.query(State).join(
        City, State.id == City.state_id).order_by(State.id, City.id).all()

    for state in query_inner:
        print("{}: {}".format(state.id, state.name))
        for cities in state.cities:
            print("\t{}: {}".format(cities.id, cities.name))

    session.close()
