#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey)
from sqlalchemy import create_engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean)
    role_id = Column(Integer, ForeignKey("roles.id"))

    # relationships
    role = relationship("Role", back_populates="auditions")

    # query methods
    def call_back(self):
        self.hired = True

    def __repr__(self):
        return '<Audition %r>' % self.id


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    # relationships
    auditions = relationship("Audition", back_populates="role")
    actors = association_proxy("auditions", "actor")
    locations = association_proxy("auditions", "location")

    # query methods

    def lead(self):
        engine = create_engine('sqlite:///theater_work.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        first_hired_audition = session.query(Audition).where(Audition.role_id == self.id).where(Audition.hired == True).first()
        session.close()
        if first_hired_audition:
            return first_hired_audition
        else:
            return 'no actor has been hired for this role'
        

    def understudy(self):
        engine = create_engine('sqlite:///theater_work.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        auditions = session.query(Audition).where(Audition.role_id == self.id).where(Audition.hired == True)
        session.close()
        try:
            second_hired_audition = auditions[1]
            return second_hired_audition
        except:
            return 'no actor has been hired for understudy for this role'

    def __repr__(self):
        return '<Role %r>' % self.character_name
