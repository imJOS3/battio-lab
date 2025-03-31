from flask import Blueprint, request, jsonify
from database import db

empleados_bp = Blueprint('empleados', __name__)

# Obtener todos los empleados
@empleados_bp.route('/', methods=['GET'])
def get_empleados():
    cursor = db.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    return jsonify(empleados)

# Crear un nuevo empleado
@empleados_bp.route('/crear', methods=['POST'])
def create_empleado():
    data = request.json
    cursor = db.connection.cursor()
    sql = "INSERT INTO empleados (nombre, apellido, correo, numeroTel, direccion, fechaIngreso, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (data['nombre'], data['apellido'], data['correo'], data['numeroTel'], data['direccion'], data['fechaIngreso'], 'Activo')
    cursor.execute(sql, values)
    db.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Empleado creado exitosamente"}), 201
