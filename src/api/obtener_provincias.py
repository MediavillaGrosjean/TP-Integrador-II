import requests
from requests.exceptions import RequestException
from logger import manejar_excepcion, registrar_actividad
from db import consultar_documentos, guardar_provincias
from utils import normalizar_texto

def obtener_provincias():
    provincias_guardadas = consultar_documentos("provincias")

    if provincias_guardadas:
        registrar_actividad(f"Las provincias ya están guardadas en la base de datos.")
        return provincias_guardadas

    url = "https://apis.datos.gob.ar/georef/api/provincias"

    try:
        response = requests.get(url)
        response.raise_for_status()
        provincias = response.json()['provincias']

        provincias_formateadas = [
            {
                "_id": provincia["id"],
                "nombre": provincia["nombre"],
                "nombre_normalizado": normalizar_texto(provincia["nombre"]),
                "centroide": provincia["centroide"]
            }
            for provincia in provincias
        ]

        registrar_actividad(f"Se obtuvieron {len(provincias)} provincias del llamado a la API.")
        guardar_provincias(provincias_formateadas)

        return provincias_formateadas
    except RequestException as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise