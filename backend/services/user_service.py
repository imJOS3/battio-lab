from database.db import get_db_connection

def get_all_users():
    """Obtiene todos los usuarios de la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def add_user(data):
    """Agrega un nuevo usuario a la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (idEmpleado, idRol, username, contrasena) VALUES (%s, %s, %s, %s)",
        (data["idEmpleado"], data["idRol"], data["username"], data["contrasena"]),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Usuario agregado correctamente"}
