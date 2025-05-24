from sqlalchemy.orm import Session
from models.PrecioManoDeObra import PrecioManoDeObra  # Ajusta según tu estructura

class PrecioManoDeObraService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def crear_precio(self, precio_data: dict) -> PrecioManoDeObra:
        nuevo_precio = PrecioManoDeObra(**precio_data)
        self.db.add(nuevo_precio)
        self.db.commit()
        self.db.refresh(nuevo_precio)
        return nuevo_precio

    def obtener_precio_por_tipo(self, tipo_servicio: str) -> PrecioManoDeObra | None:
        return self.db.query(PrecioManoDeObra).filter(PrecioManoDeObra.tipoServicio == tipo_servicio).first()

    def listar_precios(self) -> list[PrecioManoDeObra]:
        return self.db.query(PrecioManoDeObra).all()

    def actualizar_precio(self, tipo_servicio: str, nuevos_datos: dict) -> PrecioManoDeObra | None:
        precio = self.obtener_precio_por_tipo(tipo_servicio)
        if not precio:
            return None
        for key, value in nuevos_datos.items():
            setattr(precio, key, value)
        self.db.commit()
        self.db.refresh(precio)
        return precio

    def eliminar_precio(self, tipo_servicio: str) -> bool:
        precio = self.obtener_precio_por_tipo(tipo_servicio)
        if not precio:
            return False
        self.db.delete(precio)
        self.db.commit()
        return True
