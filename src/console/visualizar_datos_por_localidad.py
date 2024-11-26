from db import consultar_por_localidad
from logger import manejar_excepcion, registrar_actividad

def visualizar_datos_por_localidad(nombre_localidad):
    localidades = consultar_por_localidad(nombre_localidad)

    if not localidades:
        manejar_excepcion(f"No se encontraron datos para la localidad: {nombre_localidad}")
        return

    print('\n#################################################################################')
    registrar_actividad(f"Datos para la consulta: {nombre_localidad}")
    print('#################################################################################\n')

    for localidad in localidades:
        registrar_actividad(f"Provincia: {localidad['provincia_nombre']}")
        registrar_actividad(f"Localidad: {localidad['nombre']}")
        registrar_actividad(f"Clima: {localidad['clima']['descripcion']}")
        registrar_actividad(f"Temperatura: {localidad['clima']['temperatura']}°C")
        registrar_actividad(f"Humedad: {localidad['clima']['humedad']}%")

