# api/clientes_api.py
import requests

BASE_URL = "http://localhost:5000/api/clientes"

def obtener_clientes():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error en la petición: {e}")
        return []

def obtener_cliente_por_id(id_cliente):
    try:
        response = requests.get(f"{BASE_URL}/{id_cliente}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener cliente por ID: {e}")
        return {}

def crear_cliente(datos):
    try:
        response = requests.post(BASE_URL, json=datos)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al crear cliente: {e}")

def modificar_cliente(id_cliente, datos):
    try:
        response = requests.put(f"{BASE_URL}/{id_cliente}", json=datos)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al modificar cliente: {e}")

def eliminar_cliente(id_cliente):
    try:
        response = requests.delete(f"{BASE_URL}/{id_cliente}")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al eliminar cliente: {e}")
