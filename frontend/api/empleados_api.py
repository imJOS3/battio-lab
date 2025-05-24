import requests

API_URL = "http://localhost:5000/empleados"

def obtener_empleados():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al obtener empleados: {e}")

def crear_empleado(data):
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al crear empleado: {e}")

def actualizar_empleado(id_empleado, data):
    try:
        response = requests.put(f"{API_URL}/{id_empleado}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al actualizar empleado con ID {id_empleado}: {e}")

def eliminar_empleado(id_empleado):
    try:
        response = requests.delete(f"{API_URL}/{id_empleado}")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al eliminar empleado con ID {id_empleado}: {e}")
