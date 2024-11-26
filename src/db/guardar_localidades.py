from .operaciones_db import insertar_documentos
from logger import manejar_excepcion, registrar_actividad

def guardar_localidades(localidades):
    try:
        insertar_documentos('localidades', localidades)
        registrar_actividad(f"Se guardaron {len(localidades)} localidades en la base de datos.")
    except Exception as e:
        manejar_excepcion(e)
        raise