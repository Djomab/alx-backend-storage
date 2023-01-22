#!/usr/bin/env python3
"""pymongo retrieving list"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    query = {"topics": topic}
    schoolst = mongo_collection.find(query)
    return schoolst
