import time
from logger import manejar_excepcion, registrar_actividad
from core import procesar_datos, procesar_consulta

def main():
    try:
        print()
        print('\t#########################################################################')
        print('\t    CONSULTA DEL CLIMA POR LOCALIDAD O LOCALIDADES DE UNA PROVINCIA')
        print('\tEn unos segundos iniciará la obtención de los datos a través de las API.')
        print('\tLuego se prodecerá al registro de los datos obtenidos en la base de datos.')
        print('\t\t     Este proceso puede demorar algunos minutos.')
        print('\t#########################################################################')
        print()
        time.sleep(7)
        registrar_actividad('Se inicia con la obtención y el procesamiento de datos.')
        print()
        procesar_datos()
        print()
        registrar_actividad('Finalización de la obtención y el procesamiento de datos.')

        print()
        print('\t#########################################################################')
        print('\t    CONSULTA DEL CLIMA POR LOCALIDAD O LOCALIDADES DE UNA PROVINCIA')
        print('\t#########################################################################')
        print()
        nombre_consulta = input("\tIngresa el nombre de una provincia o localidad para consultar: ").strip()
        if nombre_consulta:
            print()
            registrar_actividad('Se inicia con la obtención y el procesamiento de la consulta ingresada.')
            print()
            procesar_consulta(nombre_consulta)
            print()
            registrar_actividad('Finalización de la obtención y el procesamiento de la consulta ingresada.')
    except Exception as e:
        manejar_excepcion(e)


if __name__ == "__main__":
    main()

