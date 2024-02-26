from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())
PUERTO = os.environ.get('MONGO_PORT')

connection_string = f"mongodb://localhost:{PUERTO}"
client = MongoClient(connection_string)

print(client)

dbs = client.list_database_names()

print(dbs)
