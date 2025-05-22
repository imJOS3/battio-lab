from flask import Blueprint, request, jsonify
from services.employee_service import (
    get_all_employees,
    get_employee_by_id,
    add_employee,
    update_employee,
    delete_employee,
)

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    employees = get_all_employees()
    return jsonify(employees)

@employee_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Empleado no encontrado"}), 404

@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    response = add_employee(data)
    return jsonify(response), 201

@employee_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def edit_employee(employee_id):
    data = request.json
    response = update_employee(employee_id, data)
    return jsonify(response)

@employee_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def remove_employee(employee_id):
    response = delete_employee(employee_id)
    return jsonify(response)
