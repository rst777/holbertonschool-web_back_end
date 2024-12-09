#!/usr/bin/env python3
"""
Script to list all databases in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    # Connexion à MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Obtenir la liste des bases de données
    database_names = client.list_database_names()

    # Afficher les noms des bases de données
    for db in database_names:
        print(db)
