# api/auth_api.py

import requests

API_URL = "http://127.0.0.1:5000/auth/login"

def login_usuario(username: str, password: str):
    data = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP al iniciar sesión: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión al iniciar sesión: {e}")
        return None
