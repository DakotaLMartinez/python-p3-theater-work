#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Role, Audition

if __name__ == '__main__':
    engine = create_engine('sqlite:///theater_work.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()

