import requests

API_URL = "http://localhost:5000/precios-mano-obra"

def obtener_precios():
    response = requests.get(API_URL)
    return response.json()

def obtener_precio_por_tipo(tipo_servicio):
    response = requests.get(f"{API_URL}/{tipo_servicio}")
    return response.json()

def crear_precio(data):
    requests.post(API_URL, json=data)

def modificar_precio(data):
    tipo = data["tipoServicio"]
    requests.put(f"{API_URL}/{tipo}", json=data)

def eliminar_precio(tipo_servicio):
    requests.delete(f"{API_URL}/{tipo_servicio}")
