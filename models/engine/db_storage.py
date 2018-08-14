#!/usr/bin/python3
'''
    Database storage system
'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

available_objects = [User, State, City, Amenity, Place, Review]


class DBStorage():
    '''
        Implementation for the DBStorage
    '''
    __engine = None
    __session = None

    def __init__(self):
        target = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"))

        self.__engine = create_engine(target, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            all method
        '''
        ret_dict = {}

        if not cls:
            for classname in available_objects:
                for item in self.__session.query(classname).all():
                    key = item.__class__.__name__ + "." + item.id
                    val = item
                    ret_dict[key] = val
        else:
            for item in self.__session.query(eval(cls)).all():
                key = item.__class__.__name__ + "." + item.id
                val = item
                ret_dict[key] = val

        return ret_dict

    def new(self, obj):
        '''
            add the object to the current database session
        '''
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        '''
            commit all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            delete from the current database session obj if not None
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            create all tables in the database
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''
             call remove() method on the private session attribute
        '''
        self.__session.close()
