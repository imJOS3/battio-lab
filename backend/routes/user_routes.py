from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.user_service import (
    get_all_users,
    get_user_by_id,
    add_user,
    update_user,
    delete_user,
)

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "Usuario no encontrado"}), 404

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    response = add_user(data)
    return jsonify(response), 201

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def edit_user(user_id):
    data = request.json
    response = update_user(user_id, data)
    return jsonify(response)

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def remove_user(user_id):
    response = delete_user(user_id)
    return jsonify(response)

