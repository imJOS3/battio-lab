import requests

API_URL = "http://localhost:5000/api/usuarios"  # Asegúrate que coincide con tu ruta backend

def obtener_usuarios():
    """
    Obtiene la lista de todos los usuarios.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error al obtener usuarios:", e)
        return None

def obtener_usuario_por_id(id_usuario):
    """
    Obtiene un usuario específico por su ID.
    """
    try:
        url = f"{API_URL}/{id_usuario}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener usuario con ID {id_usuario}:", e)
        return None

def crear_usuario(data_usuario):
    """
    Crea un nuevo usuario.

    data_usuario: dict con claves:
    {
        "idEmpleado": int,
        "idRol": int,
        "username": str,
        "password": str
    }
    """
    try:
        response = requests.post(API_URL, json=data_usuario)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error al crear usuario:", e)
        return None

def actualizar_usuario(id_usuario, nuevos_datos):
    """
    Actualiza los datos del usuario con el ID especificado.

    nuevos_datos: dict con claves opcionales:
    {
        "idEmpleado": int,
        "idRol": int,
        "username": str,
        "password": str
    }
    """
    try:
        url = f"{API_URL}/{id_usuario}"
        response = requests.put(url, json=nuevos_datos)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al actualizar usuario con ID {id_usuario}:", e)
        return None

def eliminar_usuario(id_usuario):
    """
    Elimina un usuario dado su ID.
    """
    try:
        url = f"{API_URL}/{id_usuario}"
        response = requests.delete(url)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Error al eliminar usuario con ID {id_usuario}:", e)
        return False
