from flask import Blueprint, request, jsonify
from services.user_service import get_all_users, add_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    response = add_user(data)
    return jsonify(response), 201
