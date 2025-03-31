from database.db import get_db_connection

def get_all_employees():
    """Obtiene todos los empleados de la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return employees

def add_employee(data):
    """Agrega un nuevo empleado a la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (nombre, apellido, correo, numeroTel, direccion, fechaIngreso, fechaSalida, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (data["nombre"], data["apellido"], data["correo"], data["numeroTel"], data["direccion"], data["fechaIngreso"], data.get("fechaSalida"), data["estado"]),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Empleado agregado correctamente"}
