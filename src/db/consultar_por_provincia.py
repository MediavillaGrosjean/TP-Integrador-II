from .operaciones_db import consultar_documentos
from logger import manejar_excepcion, registrar_actividad
from utils import normalizar_texto

def consultar_por_provincia(nombre_provincia):
    try:
        provincia_normalizada = normalizar_texto(nombre_provincia)
        provincia = consultar_documentos('provincias', {"nombre_normalizado": provincia_normalizada})

        if provincia:
            provincia = provincia[0]
            registrar_actividad(f"Se obtuvo la provincia {provincia['nombre']} de la base de datos.")
            localidad_ids = [localidad["_id"] for localidad in consultar_documentos("localidades", {"provincia_nombre_normalizado": provincia_normalizada})]

            localidades = consultar_documentos("localidades", {"_id": {"$in": localidad_ids}})
            registrar_actividad(f"Se obtuvieron {len(localidades)} localidades de la provincia {provincia['nombre']}.")

            for localidad in localidades:
                localidad["clima"] = consultar_documentos("clima", {"lat": localidad['centroide']['lat'], "lon": localidad['centroide']['lon']})

            registrar_actividad(f"Se obtuvo el clima para las {len(localidades)} localidades de la provincia {provincia['nombre']}.")

            return {
                "provincia": provincia,
                "localidades": localidades
            }
        else:
            return None

    except Exception as e:
        manejar_excepcion(e)
        return None
