from pymongo import MongoClient
from os import environ as env

connection = MongoClient(env["MONGO_URI"])