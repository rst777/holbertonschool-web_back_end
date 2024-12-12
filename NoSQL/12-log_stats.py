#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

def get_nginx_stats():
    """Retrieve and display stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")


    # Count of each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # Methods header
    print("Methods:")
    for method in methods:

        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of status checks
    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    get_nginx_stats()

