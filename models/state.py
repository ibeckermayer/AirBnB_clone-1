#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


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
        cits = models.storage.all('City').values()
        cits_by_state = [city for city in cits if city.state_id == self.id]
        return cits_by_state
