from api import obtener_provincias, obtener_localidades, obtener_clima

def procesar_datos():
    provincias = obtener_provincias()

    for provincia in provincias:
            localidades = obtener_localidades(provincia['nombre'])

            for localidad in localidades:
                obtener_clima(localidad['centroide']['lat'], localidad['centroide']['lon'])