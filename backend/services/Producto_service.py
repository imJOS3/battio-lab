from sqlalchemy.orm import Session
from models.Producto import Producto  # Asegúrate que este import apunta correctamente a tu clase Producto

class ProductoService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def crear_producto(self, producto_data: dict) -> Producto:
        nuevo_producto = Producto(**producto_data)
        self.db.add(nuevo_producto)
        self.db.commit()
        self.db.refresh(nuevo_producto)
        return nuevo_producto

    def obtener_producto_por_id(self, id_implemento: int) -> Producto | None:
        return self.db.query(Producto).filter(Producto.ID_Implemento == id_implemento).first()

    def listar_productos(self) -> list[Producto]:
        return self.db.query(Producto).all()

    def actualizar_producto(self, id_implemento: int, nuevos_datos: dict) -> Producto | None:
        producto = self.obtener_producto_por_id(id_implemento)
        if not producto:
            return None
        for key, value in nuevos_datos.items():
            setattr(producto, key, value)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def eliminar_producto(self, id_implemento: int) -> bool:
        producto = self.obtener_producto_por_id(id_implemento)
        if not producto:
            return False
        self.db.delete(producto)
        self.db.commit()
        return True
