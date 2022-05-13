#!/usr/bin/python3

'''File with the class Place'''
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

# if getenv('HBNB_TYPE_STORAGE') == 'db':
place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id')),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id')))


class Place(BaseModel, Base):
    '''Place Class'''

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        amenity_ids = []

        @property
        def reviews(self):
            reviews = models.storage.all('Review')
            list_review = []
            for review in reviews.values():
                if review.place_id == self.id:
                    list_review.append(review)
            return (list_review)

        @property
        def amenities(self, ameni=None):
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(ameni.id)
            if self.amenity_ids.count(ameni.id) == 1:
                dict_obj = models.storage.all("Amenity")
                for obj in dict_obj.values():
                    if ameni.id == obj.id:
                        self.amenity_ids.pop()
                        break
            return (self.amenity_ids)

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default='NULL')
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True, default=0.000)
    longitude = Column(Float(), nullable=True, default=0.000)

    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    reviews = relationship('Review', backref='place')
    amenities = relationship('Amenity',
                             secondary='place_amenity',
                             back_populates='place_amenities',
                             viewonly=False)
