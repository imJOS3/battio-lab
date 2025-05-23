import requests

API_URL = "http://localhost:5000/productos"

def obtener_productos():
    response = requests.get(API_URL)
    return response.json()

def crear_producto(data):
    response = requests.post(API_URL, json=data)
    return response.json()

def actualizar_producto(id_producto, data):
    response = requests.put(f"{API_URL}/{id_producto}", json=data)
    return response.json()

def eliminar_producto(id_producto):
    response = requests.delete(f"{API_URL}/{id_producto}")
    return response.ok
