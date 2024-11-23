import requests
from requests.exceptions import RequestException
from requests.utils import quote
from logger import manejar_excepcion, registrar_actividad
from db import consultar_documentos, guardar_localidades
from utils import normalizar_texto

def obtener_localidades(nombre_provincia):
    provincia_nombre_normalizado = normalizar_texto(nombre_provincia)

    localidades_guardadas = consultar_documentos("localidades", {"provincia_nombre_normalizado": provincia_nombre_normalizado})

    if localidades_guardadas:
        registrar_actividad(f"Las localidades de la provincia {nombre_provincia} ya están guardadas.")
        return localidades_guardadas
    
    provincia_quote = quote(provincia_nombre_normalizado)

    url = f"https://apis.datos.gob.ar/georef/api/municipios?provincia={provincia_quote}&max=5000"

    try:
        response = requests.get(url)
        response.raise_for_status()
        localidades = response.json()['municipios']

        if not localidades:
            url = f"https://apis.datos.gob.ar/georef/api/localidades?provincia={provincia_quote}&max=5000"
            response = requests.get(url)
            response.raise_for_status()
            localidades = response.json()['localidades']

        localidades_formateadas = [
            {
                "_id": localidad["id"],
                "nombre": localidad["nombre"],
                "nombre_normalizado": normalizar_texto(localidad["nombre"]),
                "centroide": localidad["centroide"],
                "provincia_id": localidad["provincia"]["id"],
                "provincia_nombre": localidad["provincia"]["nombre"],
                "provincia_nombre_normalizado": normalizar_texto(localidad["provincia"]["nombre"])
            }
            for localidad in localidades
        ]

        if localidades_formateadas:
            registrar_actividad(f"Se obtuvieron {len(localidades_formateadas)} localidades de la provincia {localidades_formateadas[0]['provincia_nombre']} desde el llamado a la API.")
            guardar_localidades(localidades_formateadas)
            return localidades_formateadas
        else:
            manejar_excepcion(f"No se encontraron localidades para la provincia {nombre_provincia}.")

    except RequestException as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise
