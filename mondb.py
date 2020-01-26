from datetime import datetime
import re
import pymongo
import gridfs
import json
import os
import dns
import pandas as pd
import logging


with open("keys.json") as jsonFile:
    data = json.load(jsonFile)
    mongoUser = data['myKeys']['mongodb_username']
    mongoPassword = data['myKeys']['mongodb_password']
    connection_uri = data['myKeys']['connection_uri']


class MongoDatabase:

    def __init__(self, db_name):
        """Create an entry point for MongoDB

        :param connection_uri: Connection string to request
        :type connection_uri: str
        :param db_name: Database name
        :type db_name: Str
        """
        uri = re.sub('<username>', mongoUser, connection_uri)
        uri = re.sub('<password>', mongoPassword, uri)
        self.client = pymongo.MongoClient(uri)
        # Create your database
        self.db = self.client[db_name]

    def insert_document(self, collection, doc):
        """Insert a document into the db.collection"""
        # Create/Access your collection
        mycol = self.db[collection]
        # Insert your document into the collection
        x = mycol.insert_one(doc)
        # Return the inserted id to verify success
        return x.inserted_id
