#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        '''
            getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id
        '''
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            cits = models.storage.all('City').values()
            cits_by_state = [city for city in cits if city.state_id == self.id]
        else:
            cits = list(models.storage.all(City).values())
            cits_by_state = list(filter((lambda c: c.state_id == self.id),
                                        cits))
        return cits_by_state
