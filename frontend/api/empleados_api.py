import requests

API_URL = "http://localhost:5000/empleados"

def obtener_empleados():
    response = requests.get(API_URL)
    return response.json()

def crear_empleado(data):
    response = requests.post(API_URL, json=data)
    return response.json()

def actualizar_empleado(id_empleado, data):
    response = requests.put(f"{API_URL}/{id_empleado}", json=data)
    return response.json()

def eliminar_empleado(id_empleado):
    response = requests.delete(f"{API_URL}/{id_empleado}")
    return response.status_code == 200
