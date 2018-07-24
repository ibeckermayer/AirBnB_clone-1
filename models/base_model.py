#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''

    def __init__(self, *args, **kwargs):
        BaseModel.id = Column(String(60),
                              primary_key=True,
                              nullable=False)
        if "created_at" in kwargs:
            BaseModel.created_at = Column(DateTime,
                                          default=datetime.strptime(
                                              kwargs["created_at"],
                                              "%Y-%m-%dT%H:%M:%S.%f"),
                                          nullable=False)
        else:
            BaseModel.created_at = Column(DateTime,
                                          default=datetime.utcnow(),
                                          nullable=False)
        if "updated_at" in kwargs:
            BaseModel.updated_at = Column(DateTime,
                                          default=datetime.strptime(
                                              kwargs["updated_at"],
                                              "%Y-%m-%dT%H:%M:%S.%f"),
                                          nullable=False)
        else:
            BaseModel.updated_at = Column(DateTime,
                                          default=datetime.utcnow(),
                                          nullable=False)

        for key, val in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, val)

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      BaseModel.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      BaseModel.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        BaseModel.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = BaseModel.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = BaseModel.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        if "_sa_instance_state" in cp_dct:
            del cp_dct["_sa_instance_state"]

        return (cp_dct)

    def delete(self):
        '''
            delete the current instance from the storage (models.storage)
            by calling the method delete
        '''
        models.storage.delete(self)
