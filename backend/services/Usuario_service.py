from sqlalchemy.orm import Session
from models.Usuario import Usuario

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db

    def crear_usuario(self, usuario_data: dict):
        usuario = Usuario(
            idEmpleado=usuario_data["idEmpleado"],
            idRol=usuario_data["idRol"],
            username=usuario_data["username"],
            password=usuario_data["password"]  # Sin hash
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
            setattr(usuario, clave, valor)

        self.db.commit()
        return usuario

    def eliminar_usuario(self, idUsuario: int):
        usuario = self.db.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
        if usuario:
            self.db.delete(usuario)
            self.db.commit()
        return usuario

    def verificar_credenciales(self, username, password):
        usuario = self.db.query(Usuario).filter_by(username=username).first()
        if usuario and password == usuario.password:
            return usuario
        return None
