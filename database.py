from pymongo import MongoClient
from os import environ as env

#connection = MongoClient(settings.mongodb_uri)
connection = env["MONGO_URI"]