from .conexion_db import obtener_conexion
from pymongo.errors import PyMongoError
from pymongo import UpdateOne
from logger import manejar_excepcion, registrar_actividad

def insertar_documentos(collection_name, documentos):
    try:
        with obtener_conexion() as db:
            collection = db[collection_name]

            if isinstance(documentos, dict):
                collection.update_one(
                    {"_id": documentos["_id"]},
                    {"$set": documentos},
                    upsert=True
                )
                registrar_actividad(f"Se insertó o actualizó un documento en la colección {collection_name}.")
            elif isinstance(documentos, list):
                operaciones = []
                for documento in documentos:
                    operaciones.append(
                        UpdateOne(
                            {"_id": documento["_id"]},
                            {"$set": documento},
                            upsert=True
                        )
                    )
                if operaciones:
                    collection.bulk_write(operaciones)
                    registrar_actividad(f"Se insertaron/actualizaron {len(operaciones)} documentos en la colección {collection_name}.")
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
            if not documentos_lista:
                return documentos_lista
            registrar_actividad(f"Se encontraron {len(documentos_lista)} documentos en la colección {collection_name}.")
            return documentos_lista
    except PyMongoError as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise
