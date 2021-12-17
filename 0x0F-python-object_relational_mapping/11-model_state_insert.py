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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)


    session.close()
