#!/usr/bin/env python3

from pymongo import MongoClient

def get_count_method_path(collection, method, path):
    return collection.count_documents({"method": method, "path": path})

def nginx_stats():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Get total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")

    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count and print documents for each method
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{count} {method}")

    # Count documents with method=GET and path=/status
    status_count = get_count_method_path(collection, "GET", "/status")
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_stats()

