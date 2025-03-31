import os
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
from database.db import get_db_connection  # Asegúrate de importar correctamente

# Cargar variables de entorno
load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def generate_token(user):
    """Genera un token JWT para el usuario."""
    access_token = create_access_token(identity=user["idUsuario"])
    return {"access_token": access_token}

def authenticate_user(username, password):
    """Verifica si el usuario existe y la contraseña es correcta."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and user["password"] == password:
        return generate_token(user)
    
    return {"error": "Credenciales incorrectas"}, 401

@jwt_required()
def get_current_user():
    """Obtiene el usuario actual autenticado con el token JWT."""
    user_id = get_jwt_identity()
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE idUsuario = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify(user)

    return jsonify({"error": "Usuario no encontrado"}), 404
