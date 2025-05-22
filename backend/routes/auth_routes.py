from flask import Blueprint, request, jsonify
from services.auth_service import authenticate_user, get_current_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    return authenticate_user(data["username"], data["password"])

@auth_bp.route("/me", methods=["GET"])
def current_user():
    return get_current_user()
