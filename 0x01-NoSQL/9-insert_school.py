#!/usr/bin/env python3
"""pymongo inserting document"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
