import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "batio_lab"
}
