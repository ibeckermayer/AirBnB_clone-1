#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "only testing db storage")
class test_DBStorage(unittest.TestCase):

    def testState(self):
        state = State(name="Isaiah")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Isaiah")

    def testCity(self):
        city = City(name="Cu7ious")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Cu7ious")

    def testPlace(self):
        place = Place(name="Place", number_rooms=5)
        if place.id in models.storage.all():
            self.assertTrue(place.number_rooms, 5)
            self.assertTrue(place.name, "Place")

    def testUser(self):
        user = User(name="K")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "K")

    def testAmenity(self):
        amenity = Amenity(name="Y")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Y")

    def testReview(self):
        review = Review(text="bad")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "bad")

    def teardown(self):
        self.session.close()
        self.session.rollback()
