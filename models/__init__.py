#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
initialize the models package"""

import os
from models.db_storage import DBStorage  # Import de la classe DBStorage
from models.file_storage import FileStorage  # Import de la classe FileStorage


if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()  # Création d'une instance DBStorage
    storage.reload()  # Rechargement des modèles depuis la base de données
else:
    storage = FileStorage()  # Création d'une instance FileStorage
    storage.reload()  # Rechargement des modèles depuis les fichiers
