from .operaciones_db import insertar_documentos
from logger import manejar_excepcion, registrar_actividad

def guardar_provincias(provincias):
    try:
        insertar_documentos('provincias', provincias)
        registrar_actividad(f"Se guardaron {len(provincias)} provincias en la base de datos.")
    except Exception as e:
        manejar_excepcion(e)
        raise
