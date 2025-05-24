import requests

API_URL = "http://localhost:5000/precios-mano-obra"

def obtener_precios():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener precios: {e}")
        return []  # Retorna lista vacía si falla

def obtener_precio_por_tipo(tipo_servicio):
    try:
        response = requests.get(f"{API_URL}/{tipo_servicio}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener precio del servicio '{tipo_servicio}': {e}")
        return None  # Retorna None si falla

def crear_precio(data):
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al crear precio: {e}")
        return None

def modificar_precio(data):
    try:
        tipo = data["tipoServicio"]
        response = requests.put(f"{API_URL}/{tipo}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al modificar precio del servicio '{tipo}': {e}")
        return None

def eliminar_precio(tipo_servicio):
    try:
        response = requests.delete(f"{API_URL}/{tipo_servicio}")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error al eliminar precio del servicio '{tipo_servicio}': {e}")
        return False
