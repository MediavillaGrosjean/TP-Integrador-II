from .operaciones_db import insertar_documentos
from logger import manejar_excepcion, registrar_actividad

def guardar_clima(clima):
    try:
        insertar_documentos('clima', [clima])
        registrar_actividad(f"Clima guardado para lat: {clima['lat']}, lon: {clima['lon']}.")
    except Exception as e:
        manejar_excepcion(e)
        raise
