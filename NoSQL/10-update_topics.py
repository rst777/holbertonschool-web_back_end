#!/usr/bin/env python3
"""Module for updating topics of a school document in MongoDB"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    Args:
    mongo_collection: pymongo collection object
    name (str): the name of the school to update
    topics (list): a list of topics to set for the school

    Returns:
    None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
