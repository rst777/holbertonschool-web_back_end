#!/usr/bin/env python3
"""Module for inserting a new school document into MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
    mongo_collection: pymongo collection object
    **kwargs: keyword arguments representing the document fields

    Returns:
    The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
