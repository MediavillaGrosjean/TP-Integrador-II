from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB

class ConexionMongo:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def __enter__(self):
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        if self.client:
            self.client.close()

def obtener_conexion():
    return ConexionMongo(MONGO_URI, MONGO_DB)