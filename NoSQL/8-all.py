#!/usr/bin/env python3
"""Module for lists all documents in a collection: """


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection

    Args:
    mongo_collection: pymongo collection object

    Returns:
    list of all documents, or empty list if no documents
    """
    return list(mongo_collection.find())
