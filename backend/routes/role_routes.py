from flask import Blueprint, request, jsonify
from services.service_role import get_all_roles, get_role_by_id, add_role, update_role, delete_role

role_bp = Blueprint("role", __name__)

@role_bp.route("/roles", methods=["GET"])
def get_roles():
    return jsonify(get_all_roles())

@role_bp.route("/roles/<int:idRol>", methods=["GET"])
def get_role(idRol):
    role = get_role_by_id(idRol)
    if role:
        return jsonify(role)
    return jsonify({"error": "Rol no encontrado"}), 404

@role_bp.route("/roles", methods=["POST"])
def create_role():
    data = request.json
    return jsonify(add_role(data)), 201

@role_bp.route("/roles/<int:idRol>", methods=["PUT"])
def modify_role(idRol):
    data = request.json
    return jsonify(update_role(idRol, data))

@role_bp.route("/roles/<int:idRol>", methods=["DELETE"])
def remove_role(idRol):
    return jsonify(delete_role(idRol))
