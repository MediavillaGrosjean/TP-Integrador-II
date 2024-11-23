from api import obtener_provincias, obtener_localidades, obtener_clima
from console import visualizar_datos_por_provincia, visualizar_datos_por_localidad
from utils import normalizar_texto

def procesar_consulta(nombre_consulta=None):
    consulta_normalizada = normalizar_texto(nombre_consulta)
    provincias = obtener_provincias()

    provincia_encontrada = None
    for provincia in provincias:
        if consulta_normalizada == provincia['nombre_normalizado']:
            provincia_encontrada = provincia
            break
    
    if provincia_encontrada:
        localidades = obtener_localidades(provincia_encontrada['nombre'])
        for localidad in localidades:
            obtener_clima(localidad['centroide']['lat'], localidad['centroide']['lon'])
        visualizar_datos_por_provincia(provincia_encontrada['nombre'])

    else:
        for provincia in provincias:
            localidades = obtener_localidades(provincia['nombre'])

            for localidad in localidades:
                if consulta_normalizada == localidad['nombre_normalizado']:
                    obtener_clima(localidad['centroide']['lat'], localidad['centroide']['lon'])
                    visualizar_datos_por_localidad(localidad['nombre'])
                    return
        print(f"No se encontró la provincia ni la localidad con el nombre '{nombre_consulta}'.")