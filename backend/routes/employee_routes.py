from flask import Blueprint, request, jsonify
from services.employee_service import get_all_employees, add_employee

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    employees = get_all_employees()
    return jsonify(employees)

@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    response = add_employee(data)
    return jsonify(response), 201
