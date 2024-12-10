#!/usr/bin/env python3
"""Module for retrieving schools by topic from MongoDB"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
    mongo_collection: pymongo collection object
    topic (str): the topic to search for

    Returns:
    list of schools that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
