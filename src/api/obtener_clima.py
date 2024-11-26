import requests
from datetime import datetime
from requests.exceptions import RequestException
from logger import manejar_excepcion, registrar_actividad
from db import consultar_documentos, guardar_clima
from config import OPENWEATHER_API_KEY

def obtener_clima(lat, lon):
    clima_existente = consultar_documentos('clima', {"lat": lat, "lon": lon})

    if clima_existente:
        registrar_actividad(f"Clima encontrado en la base de datos para lat: {lat}, lon: {lon}.")
        return clima_existente[0]

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url)
        response.raise_for_status()
        clima_data = response.json()
        clima = {
            "_id": f"{lat}_{lon}",
            "lat": lat,
            "lon": lon,
            "temperatura": clima_data["main"]["temp"],
            "humedad": clima_data["main"]["humidity"],
            "descripcion": clima_data["weather"][0]["description"],
            "fecha_actualizacion": datetime.now()
        }
        registrar_actividad(f"Clima obtenido desde la API para lat: {lat}, lon: {lon}.")
        guardar_clima(clima)
        return clima
    except RequestException as e:
        manejar_excepcion(e)
        raise
    except Exception as e:
        manejar_excepcion(e)
        raise
