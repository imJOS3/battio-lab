from database.db import get_db_connection
from models.role import Role

def get_all_roles():
    """Obtiene todos los roles de la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Role(**role).to_dict() for role in roles]

def get_role_by_id(idRol):
    """Obtiene un rol por su ID."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM roles WHERE idRol = %s", (idRol,))
    role = cursor.fetchone()
    cursor.close()
    conn.close()
    return Role(**role).to_dict() if role else None

def add_role(data):
    """Agrega un nuevo rol a la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO roles (nombreRol) VALUES (%s)",
        (data["nombreRol"],),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Rol agregado correctamente"}

def update_role(idRol, data):
    """Actualiza un rol en la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE roles SET nombreRol = %s WHERE idRol = %s",
        (data["nombreRol"], idRol),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Rol actualizado correctamente"}

def delete_role(idRol):
    """Elimina un rol de la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM roles WHERE idRol = %s", (idRol,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Rol eliminado correctamente"}
