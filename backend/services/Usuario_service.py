from sqlalchemy.orm import Session
from models.Usuario import Usuario
from utils.security import hash_password, verify_password

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db

    def crear_usuario(self, usuario_data: dict):
        usuario = Usuario(
            idEmpleado=usuario_data["idEmpleado"],
            idRol=usuario_data["idRol"],
            username=usuario_data["username"],
            password=hash_password(usuario_data["password"])
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def obtener_usuario_por_username(self, username: str):
        return self.db.query(Usuario).filter(Usuario.username == username).first()

    def obtener_usuarios(self):
        return self.db.query(Usuario).all()

    def actualizar_usuario(self, idUsuario: int, datos_actualizados: dict):
        usuario = self.db.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
        if not usuario:
            return None
        for clave, valor in datos_actualizados.items():
            if clave == "password":
                valor = hash_password(valor)
            setattr(usuario, clave, valor)
        self.db.commit()
        return usuario

    def eliminar_usuario(self, idUsuario: int):
        usuario = self.db.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
        if usuario:
            self.db.delete(usuario)
            self.db.commit()
        return usuario
