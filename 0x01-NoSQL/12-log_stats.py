#!/usr/bin/env python3
"""MongoDB Operations with Python using pymongo"""
from pymongo import MongoClient


def stats_logs() -> None:
    """
    Function that provides some stats about Nginx logs
    stored in MongoDB.
    Returns:
        Stats about Nginx logs.
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    myclient = MongoClient("mongodb://localhost:27017/")
    my_database = myclient["logs"]
    nginx = my_database["nginx"]
    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, nginx.count_documents({"method": method}))
        )

    print(
        "{} status check".format(
            nginx.count_documents({"method": "GET", "path": "/status"}))
    )


if __name__ == "__main__":
    stats_logs()
