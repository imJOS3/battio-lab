# from flask import Blueprint, request, jsonify
# from pydantic import ValidationError
# from sqlalchemy.orm import Session
# from models import Cliente  # Ajusta según tu estructura
# from services.Cliente_service import ClienteService  # El servicio que ya tienes
# from schemas.Cliente_schema import ClienteCreate, ClienteUpdate, ClienteOut  # Los modelos Pydantic
# from database import get_db  # Función para obtener la sesión de DB, ajústala según tu setup

# cliente_bp = Blueprint('clientes', __name__, url_prefix='/clientes')

# # @cliente_bp.route("/", methods=["POST"])
# def crear_cliente():
#     db: Session = get_db()
#     try:
#         data = ClienteCreate(**request.json)
#     except ValidationError as e:
#         return jsonify({"error": e.errors()}), 400

#     service = ClienteService(db)
#     nuevo_cliente = service.crear_cliente(data.dict())
#     cliente_out = ClienteOut.from_orm(nuevo_cliente)
#     return jsonify(cliente_out.dict()), 201

# @cliente_bp.route("/", methods=["GET"])
# def listar_clientes():
#     db: Session = get_db()
#     service = ClienteService(db)
#     clientes = service.listar_clientes()
#     clientes_out = [ClienteOut.from_orm(c).dict() for c in clientes]
#     return jsonify(clientes_out), 200

# @cliente_bp.route("/<int:idCliente>", methods=["GET"])
# def obtener_cliente(idCliente: int):
#     db: Session = get_db()
#     service = ClienteService(db)
#     cliente = service.obtener_cliente_por_id(idCliente)
#     if not cliente:
#         return jsonify({"error": "Cliente no encontrado"}), 404
#     cliente_out = ClienteOut.from_orm(cliente)
#     return jsonify(cliente_out.dict()), 200

# @cliente_bp.route("/<int:idCliente>", methods=["PUT"])
# def actualizar_cliente(idCliente: int):
#     db: Session = get_db()
#     service = ClienteService(db)
#     try:
#         data = ClienteUpdate(**request.json)
#     except ValidationError as e:
#         return jsonify({"error": e.errors()}), 400

#     cliente_actualizado = service.actualizar_cliente(idCliente, data.dict(exclude_unset=True))
#     if not cliente_actualizado:
#         return jsonify({"error": "Cliente no encontrado"}), 404
#     cliente_out = ClienteOut.from_orm(cliente_actualizado)
#     return jsonify(cliente_out.dict()), 200

# @cliente_bp.route("/<int:idCliente>", methods=["DELETE"])
# def eliminar_cliente(idCliente: int):
#     db: Session = get_db()
#     service = ClienteService(db)
#     resultado = service.eliminar_cliente(idCliente)
#     if not resultado:
#         return jsonify({"error": "Cliente no encontrado"}), 404
#     return jsonify({"message": "Cliente eliminado (soft delete) correctamente"}), 200
