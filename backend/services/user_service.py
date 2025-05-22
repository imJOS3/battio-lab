from database.db import get_db_connection
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE idUsuario = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def add_user(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.generate_password_hash(data["contrasena"]).decode("utf-8")  # Encriptar contraseña
    cursor.execute(
        "INSERT INTO users (idEmpleado, idRol, username, contrasena) VALUES (%s, %s, %s, %s)",
        (data["idEmpleado"], data["idRol"], data["username"], hashed_password),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Usuario agregado correctamente"}

def update_user(user_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.generate_password_hash(data["contrasena"]).decode("utf-8")  # Encriptar nueva contraseña
    cursor.execute(
        "UPDATE users SET idEmpleado = %s, idRol = %s, username = %s, contrasena = %s WHERE idUsuario = %s",
        (data["idEmpleado"], data["idRol"], data["username"], hashed_password, user_id),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Usuario actualizado correctamente"}

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE idUsuario = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Usuario eliminado correctamente"}

def login_user(username, password):
    """Autentica al usuario y devuelve un token JWT si las credenciales son correctas."""
    user = get_user_by_username(username)
    if user and bcrypt.check_password_hash(user["contrasena"], password):
        access_token = create_access_token(identity=user["idUsuario"])
        return {"token": access_token, "message": "Inicio de sesión exitoso"}
    
    return {"message": "Credenciales incorrectas"}, 401
