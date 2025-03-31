from flask import Blueprint, request, jsonify
from database import db

usuarios_bp = Blueprint('usuarios', __name__)

# Obtener todos los usuarios
@usuarios_bp.route('/', methods=['GET'])
def get_usuarios():
    cursor = db.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    return jsonify(usuarios)

# Crear un usuario
@usuarios_bp.route('/crear', methods=['POST'])
def create_usuario():
    data = request.json
    cursor = db.connection.cursor()
    sql = "INSERT INTO usuarios (nombre, correo, contraseña, rol) VALUES (%s, %s, %s, %s)"
    values = (data['nombre'], data['correo'], data['contraseña'], data['rol'])
    cursor.execute(sql, values)
    db.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201
