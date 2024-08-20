import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)
    birth_year = Column(String(250), nullable=True)
    planets = Column(String(250), ForeignKey('planets.id'))
    starships = Column(String(250), ForeignKey('starships.id'))

class FavCharacters(Base):
    __tablename__ = 'favcharacters'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=True)
    rotation_period = Column(String(250), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

class FavPlanets(Base):
    __tablename__ = 'favplanets'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=True)
    speed = Column(String(250), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
