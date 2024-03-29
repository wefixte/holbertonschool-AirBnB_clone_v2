#!/usr/bin/python3
""" State Module for HBNB project
holds class Amenity
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    subclass - Amenity : inherits from BaseModel
    """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attribute:
        name - string - empty string
        """
        super().__init__(*args, **kwargs)
