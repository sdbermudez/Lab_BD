import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os


def conectar():
    # Leer credenciales desde variables de entorno
    
    dotenv_path = Path(__file__).resolve().parents[1] / 'credenciales.env'
    # Cargar el archivo .env si existe, de lo contrario cargar las variables de entorno del sistema
    if dotenv_path.exists():
        load_dotenv(dotenv_path=dotenv_path)
    else:
        load_dotenv()
    
    usuario = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    host = os.getenv('PG_HOST', 'localhost')
    puerto = int(os.getenv('PG_PORT', '5432'))
    nombre_bd = os.getenv('PG_DATABASE')

    # Crear engine de SQLAlchemy
    engine = create_engine(
        f"postgresql+psycopg2://{usuario}:{password}@{host}:{puerto}/{nombre_bd}",
        connect_args={'client_encoding': 'utf8'}
    )
    return engine

