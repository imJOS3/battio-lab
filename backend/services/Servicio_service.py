from sqlalchemy.orm import Session
from models.Servicio import Servicio  # Asegúrate que el import apunte a tu modelo real
from datetime import datetime

class ServicioService:
    def __init__(self, db: Session):
        self.db = db

    def crear_servicio(self, id_cliente: int, id_empleado: int, tipo_servicio: str, fecha_ingreso: datetime, fecha_entrega: datetime = None, observaciones: str = None) -> Servicio:
        nuevo_servicio = Servicio(
            idCliente=id_cliente,
            idEmpleado=id_empleado,
            tipoServicio=tipo_servicio,
            fechaIngreso=fecha_ingreso,
            fechaEntrega=fecha_entrega,
            observaciones=observaciones
        )
        self.db.add(nuevo_servicio)
        self.db.commit()
        self.db.refresh(nuevo_servicio)
        return nuevo_servicio

    def obtener_servicio_por_id(self, id_servicio: int) -> Servicio | None:
        return self.db.query(Servicio).filter(Servicio.idServicio == id_servicio).first()

    def listar_servicios(self) -> list[Servicio]:
        return self.db.query(Servicio).all()

    def actualizar_servicio(self, id_servicio: int, **datos_actualizados) -> Servicio | None:
        servicio = self.obtener_servicio_por_id(id_servicio)
        if not servicio:
            return None
        for key, value in datos_actualizados.items():
            if hasattr(servicio, key):
                setattr(servicio, key, value)
        self.db.commit()
        self.db.refresh(servicio)
        return servicio

    def eliminar_servicio(self, id_servicio: int) -> bool:
        servicio = self.obtener_servicio_por_id(id_servicio)
        if not servicio:
            return False
        self.db.delete(servicio)
        self.db.commit()
        return True
