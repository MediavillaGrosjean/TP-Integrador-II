import requests
from requests.exceptions import RequestException
from logger import manejar_excepcion, registrar_actividad
from config import OPENWEATHER_API_KEY

def obtener_clima(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url)
        response.raise_for_status()
        clima = response.json()
        registrar_actividad(f"Clima obtenido para lat: {lat}, lon: {lon}.")
        return clima
    except RequestException as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise
