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

def get_employee_by_id(employee_id):
    """Obtiene un empleado por su ID."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE idEmpleados = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()
    return employee

def add_employee(data):
    """Agrega un nuevo empleado a la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO employees (nombre, apellido, correo, numeroTel, direccion, fechaIngreso, fechaSalida, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (data["nombre"], data["apellido"], data["correo"], data["numeroTel"], data["direccion"],
         data["fechaIngreso"], data.get("fechaSalida"), data["estado"]),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Empleado agregado correctamente"}

def update_employee(employee_id, data):
    """Actualiza un empleado existente."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE employees
        SET nombre = %s, apellido = %s, correo = %s, numeroTel = %s, direccion = %s, fechaIngreso = %s, fechaSalida = %s, estado = %s
        WHERE idEmpleados = %s
        """,
        (data["nombre"], data["apellido"], data["correo"], data["numeroTel"], data["direccion"],
         data["fechaIngreso"], data.get("fechaSalida"), data["estado"], employee_id),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Empleado actualizado correctamente"}

def delete_employee(employee_id):
    """Elimina un empleado de la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE idEmpleados = %s", (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Empleado eliminado correctamente"}
