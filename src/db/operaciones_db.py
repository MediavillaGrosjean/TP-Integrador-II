from conexion_db import obtener_conexion
from pymongo.errors import PyMongoError
from logger import manejar_excepcion
from logger import registrar_actividad

def insertar_documentos(collection_name, documentos):
    try:
        with obtener_conexion() as db:
            collection = db[collection_name]
            if isinstance(documentos, list):
                collection.insert_many(documentos)
                registrar_actividad(f"Se insertaron {len(documentos)} documentos en la colección {collection_name}.")
            else:
                collection.insert_one(documentos)
                registrar_actividad(f"Se insertó un documento en la colección {collection_name}.")
    except PyMongoError as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise

def consultar_documentos(collection_name, query={}):
    try:
        with obtener_conexion() as db:
            collection = db[collection_name]
            documentos = collection.find(query)
            documentos_lista = list(documentos)
            registrar_actividad(f"Se encontraron {len(documentos_lista)} documentos en la colección {collection_name}.")
            return documentos_lista
    except PyMongoError as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise
