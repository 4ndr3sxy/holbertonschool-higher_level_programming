#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    flag = False
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).filter(State.name == sys.argv[4]).order_by(State.id)
    for state in session.query(State).filter(State.name == sys.argv[4]).order_by(State.id):
        flag = True
        print("{}".format(state.id, state.name))
    if flag is False:
        print("Not found")


    session.close()
