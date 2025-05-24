from sqlalchemy.orm import Session
from models.Empleado import Empleado  # Ajusta la ruta según tu estructura de proyecto

class EmpleadoService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def crear_empleado(self, empleado_data: dict) -> Empleado:
        nuevo_empleado = Empleado(**empleado_data)
        self.db.add(nuevo_empleado)
        self.db.commit()
        self.db.refresh(nuevo_empleado)
        return nuevo_empleado

    def obtener_empleado_por_id(self, idEmpleado: int) -> Empleado | None:
        return self.db.query(Empleado).filter(Empleado.idEmpleado == idEmpleado).first()

    def listar_empleados(self) -> list[Empleado]:
        return self.db.query(Empleado).filter(Empleado.estado == True).all()

    def actualizar_empleado(self, idEmpleado: int, nuevos_datos: dict) -> Empleado | None:
        empleado = self.obtener_empleado_por_id(idEmpleado)
        if not empleado:
            return None
        for key, value in nuevos_datos.items():
            setattr(empleado, key, value)
        self.db.commit()
        self.db.refresh(empleado)
        return empleado

    def eliminar_empleado(self, idEmpleado: int) -> bool:
        empleado = self.obtener_empleado_por_id(idEmpleado)
        if not empleado:
            return False
        # Soft delete: cambiar estado a False
        empleado.estado = False
        self.db.commit()
        return True
