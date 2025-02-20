#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic."""
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools that have the specific topic in their topics."""
    return mongo_collection.find({'topics': topic})
