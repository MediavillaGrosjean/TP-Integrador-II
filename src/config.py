import os
from logger import manejar_excepcion

def cargar_variables_entorno():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(base_dir, '..', '.env')

        with open(env_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()
    except FileNotFoundError:
        raise FileNotFoundError("El archivo .env no se encuentra.")
    except Exception as e:
        manejar_excepcion(e)
        raise

cargar_variables_entorno()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
