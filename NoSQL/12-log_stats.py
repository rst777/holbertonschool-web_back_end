#!/usr/bin/python3
"""Script pour fournir des statistiques sur les logs Nginx stockés dans MongoDB"""
from pymongo import MongoClient

def log_stats():
    """Récupérer et afficher les statistiques des logs Nginx"""
    # Connexion à MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Sélectionner la base de données logs et la collection nginx
    collection = client.logs.nginx

    # Nombre total de logs
    total_logs = collection.count_documents({})

    # Méthodes à vérifier
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Afficher le nombre total de logs
    print(f"{total_logs} logs")

    # Afficher l'en-tête des méthodes
    print("Methods:")

    # Compter et afficher les statistiques pour chaque méthode
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Compter les vérifications de statut
    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    log_stats()
