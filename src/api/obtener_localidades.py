import requests
from requests.exceptions import RequestException
from logger import manejar_excepcion, registrar_actividad
from db import consultar_documentos

def obtener_localidades(provincia_id):
    localidades_guardadas = consultar_documentos("localidades", {"provincia_id": provincia_id})

    if localidades_guardadas:
        registrar_actividad(f"Las localidades de la provincia {provincia_id} ya están guardadas.")
        return localidades_guardadas

    url = f"https://apis.datos.gob.ar/georef/api/municipios?provincia={provincia_id}&max=5000"

    try:
        response = requests.get(url)
        response.raise_for_status()
        localidades = response.json()['municipios']
        registrar_actividad(f"Se obtuvieron {len(localidades)} localidades de la provincia {provincia_id}.")
        return localidades
    except RequestException as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise
