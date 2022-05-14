#!/usr/bin/python3

'''File with the class State'''
from os import getenv
import models
from models.state import State
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    '''State Class'''

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state')

    if storage != 'db':
        @property
        def cities(self):
            cities = models.storage.all(State)
            list_city = []
            for city in cities.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return (list_city)
