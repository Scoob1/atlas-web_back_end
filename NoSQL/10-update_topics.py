#!/usr/bin/env python3
"""Module to update the topics of a school document based on the name."""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document based on the school name."""
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )
