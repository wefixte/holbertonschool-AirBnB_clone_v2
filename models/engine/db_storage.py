#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""

import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
	"""
    This class represents the storage engine for the AirBnB project. 
    It uses SQLAlchemy to interact with a MySQL database.

    Attributes:
        __engine (sqlalchemy.Engine): The Engine object used to interact with the database.
        __session (sqlalchemy.orm.session.Session): The Session object used to manage database transactions.
        __classes (list): A list of model classes that will be managed by this storage engine.
    """
	__engine = None
	__session = None
	__classes = [User, State, City, Place, Review, Amenity]

	def __init__(self):
		"""Initialize a new DBStorage instance."""
		user = os.environ.get('HBNB_MYSQL_USER')
		passwd = os.environ.get('HBNB_MYSQL_PWD')
		host = os.environ.get('HBNB_MYSQL_HOST')
		database = os.environ.get('HBNB_MYSQL_DB')
		db_env = os.environ.get('HBNB_ENV')

		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
									  format(user, passwd, host, database),
									  pool_pre_ping=True)
		
		if db_env == 'test':
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""
    	Returns a dictionary of models currently in storage. If a class is provided, 
    	it returns all instances of that class; if no class is provided, it returns 
    	all instances of all classes in storage.

    	Args:
        	cls (BaseModel, optional): The class to retrieve instances of. If None, 
        	instances of all classes will be retrieved.

    	Returns:
        	dict: A dictionary where the keys are strings in the format '<class name>.<id>', 
        	and the values are the corresponding instances.
    	"""
		if cls is not None:
			object = {}
			for val in self.__session.query(cls).all():
				key = val.__class__.__name__ + '.' + val.id
				object[key] = val
			return object
		else:
			classes = self.__classes
			for val in self.__session.query(classes).all():
				key = val.__class__.__name__ + '.' + val.id
				object[key] = val
			return object
		
	def new(self, obj):
		"""
		Adds a new model instance to the database.

		Args:
			obj (BaseModel): The model instance to add.
		"""
		self.__session.add(obj)

	def save(self):
		"""
		Commits all changes to the database.
		"""
		self.__session.commit()

	def delete(self, obj=None):
		"""
		Deletes a model instance from the database.

		Args:
			obj (BaseModel, optional): The model instance to delete.
		"""
		if obj is not None:
			self.__session.delete(obj)
	
	def reload(self):
		"""
		Reloads models from the database.
		"""
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine,
								 	expire_on_commit=False)
		Session = scoped_session(session_factory)
		self.__session = Session()

	def close(self):
		"""Close the current session."""
		self.__session.remove()
