from sqlalchemy.orm import Session
from models.Rol import Rol  # Ajusta el import según tu estructura real

class RolService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def crear_rol(self, nombre_rol: str) -> Rol:
        nuevo_rol = Rol(nombreRol=nombre_rol)
        self.db.add(nuevo_rol)
        self.db.commit()
        self.db.refresh(nuevo_rol)
        return nuevo_rol

    def obtener_rol_por_id(self, id_rol: int) -> Rol | None:
        return self.db.query(Rol).filter(Rol.idRol == id_rol).first()

    def obtener_rol_por_nombre(self, nombre_rol: str) -> Rol | None:
        return self.db.query(Rol).filter(Rol.nombreRol == nombre_rol).first()

    def listar_roles(self) -> list[Rol]:
        return self.db.query(Rol).all()

    def actualizar_rol(self, id_rol: int, nuevo_nombre: str) -> Rol | None:
        rol = self.obtener_rol_por_id(id_rol)
        if not rol:
            return None
        rol.nombreRol = nuevo_nombre
        self.db.commit()
        self.db.refresh(rol)
        return rol

    def eliminar_rol(self, id_rol: int) -> bool:
        rol = self.obtener_rol_por_id(id_rol)
        if not rol:
            return False
        self.db.delete(rol)
        self.db.commit()
        return True
