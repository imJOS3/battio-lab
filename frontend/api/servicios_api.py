# api/servicios_api.py
import requests

BASE_URL = "http://localhost:5000/api/servicios"

def obtener_servicios():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener servicios: {e}")
        return []

def obtener_servicio_por_id(id_servicio):
    try:
        response = requests.get(f"{BASE_URL}/{id_servicio}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener servicio por ID: {e}")
        return {}

def crear_servicio(datos):
    try:
        response = requests.post(BASE_URL, json=datos)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al crear servicio: {e}")
        raise

def modificar_servicio(datos):
    try:
        response = requests.put(f"{BASE_URL}/{datos['idServicio']}", json=datos)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al modificar servicio: {e}")
        raise

def eliminar_servicio(id_servicio):
    try:
        response = requests.delete(f"{BASE_URL}/{id_servicio}")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al eliminar servicio: {e}")
        raise
