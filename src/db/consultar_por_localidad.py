from .operaciones_db import consultar_documentos
from logger import manejar_excepcion, registrar_actividad
from utils import normalizar_texto

def consultar_por_localidad(nombre_localidad):
    try:
        localidad_normalizada = normalizar_texto(nombre_localidad)

        localidades = consultar_documentos('localidades', {"nombre_normalizado": localidad_normalizada})

        if localidades:

            registrar_actividad(f"Se encontraron {len(localidades)} localidades con el nombre {localidad_normalizada}.")

            for localidad in localidades:
                clima = consultar_documentos('clima', {"lat": localidad['centroide']['lat'], "lon": localidad['centroide']['lon']})

                if clima:
                    localidad["clima"] = clima[0]

            registrar_actividad(f"Se obtuvo el clima para las {len(localidades)} localidades con el nombre {localidad_normalizada}.")

            return localidades
        else:
            return None

    except Exception as e:
        manejar_excepcion(e)
        return None
