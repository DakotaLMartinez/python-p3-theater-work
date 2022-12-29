#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Role, Audition


if __name__ == '__main__':
    engine = create_engine('sqlite:///theater_work.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Role).delete()
    session.query(Audition).delete()
    
    # Script goes here!

    # Roles
    hamlet = Role(character_name='Hamlet')
    ophelia = Role(character_name='Ophelia')

    session.add_all([hamlet, ophelia])

    session.commit()

    # Auditions
    dakota = Audition(
        actor='Dakota',
        location='Lancaster',
        phone=55555555,
        hired=True,
        role_id=hamlet.id
    )
    sandra = Audition(
        actor='Sandra',
        location='Palmdale',
        phone=44444444,
        hired=True,
        role_id=ophelia.id
    )

    session.add_all([dakota, sandra])

    session.commit()
