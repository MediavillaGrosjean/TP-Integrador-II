import requests
from requests.exceptions import RequestException
from logger import manejar_excepcion, registrar_actividad

def obtener_provincias():
    url = "https://apis.datos.gob.ar/georef/api/provincias"
    try:
        response = requests.get(url)
        response.raise_for_status()
        provincias = response.json()['provincias']
        registrar_actividad(f"Se obtuvieron {len(provincias)} provincias.")
        return provincias
    except RequestException as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise