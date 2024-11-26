from db import consultar_por_provincia
from logger import manejar_excepcion, registrar_actividad

def visualizar_datos_por_provincia(nombre_provincia):
    datos = consultar_por_provincia(nombre_provincia)

    if not datos:
        manejar_excepcion(f"No se encontraron datos para la provincia: {nombre_provincia}")
        return

    print('\n#################################################################################')
    registrar_actividad(f"Datos para la consulta: {nombre_provincia}")
    print('#################################################################################\n')

    for localidad in datos['localidades']:
        registrar_actividad(f"Provincia: {localidad['provincia_nombre']}")
        registrar_actividad(f"Localidad: {localidad['nombre']}")
        registrar_actividad(f"Clima: {localidad['clima'][0]['descripcion']}")
        registrar_actividad(f"Temperatura: {localidad['clima'][0]['temperatura']}°C.")
        registrar_actividad(f"Humedad: {localidad['clima'][0]['humedad']}%\n")
