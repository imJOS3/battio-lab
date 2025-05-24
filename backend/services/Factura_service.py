from sqlalchemy.orm import Session
from models.Factura import Factura  # Ajusta la importación según la estructura de tu proyecto

class FacturaService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def crear_factura(self, factura_data: dict) -> Factura:
        nueva_factura = Factura(**factura_data)
        self.db.add(nueva_factura)
        self.db.commit()
        self.db.refresh(nueva_factura)
        return nueva_factura

    def obtener_factura_por_id(self, idFactura: int) -> Factura | None:
        return self.db.query(Factura).filter(Factura.idFactura == idFactura).first()

    def listar_facturas(self) -> list[Factura]:
        return self.db.query(Factura).all()

    def actualizar_factura(self, idFactura: int, nuevos_datos: dict) -> Factura | None:
        factura = self.obtener_factura_por_id(idFactura)
        if not factura:
            return None
        for key, value in nuevos_datos.items():
            setattr(factura, key, value)
        self.db.commit()
        self.db.refresh(factura)
        return factura

    def eliminar_factura(self, idFactura: int) -> bool:
        factura = self.obtener_factura_por_id(idFactura)
        if not factura:
            return False
        self.db.delete(factura)
        self.db.commit()
        return True
