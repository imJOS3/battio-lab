from sqlalchemy.orm import Session
from models.Clientes import Cliente  # Ajusta la importación según tu estructura

class ClienteService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def crear_cliente(self, cliente_data: dict) -> Cliente:
        nuevo_cliente = Cliente(**cliente_data)
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)
        return nuevo_cliente

    def obtener_cliente_por_id(self, idCliente: int) -> Cliente | None:
        return self.db.query(Cliente).filter(Cliente.idCliente == idCliente).first()

    def listar_clientes(self) -> list[Cliente]:
        return self.db.query(Cliente).filter(Cliente.estado == True).all()

    def actualizar_cliente(self, idCliente: int, nuevos_datos: dict) -> Cliente | None:
        cliente = self.obtener_cliente_por_id(idCliente)
        if not cliente:
            return None
        for key, value in nuevos_datos.items():
            if hasattr(cliente, key):
                setattr(cliente, key, value)
        self.db.commit()
        self.db.refresh(cliente)
        return cliente

    def eliminar_cliente(self, idCliente: int) -> bool:
        cliente = self.obtener_cliente_por_id(idCliente)
        if not cliente:
            return False
        # En lugar de eliminar, cambiamos estado a False (soft delete)
        cliente.estado = False
        self.db.commit()
        return True
