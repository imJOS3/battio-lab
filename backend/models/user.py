class User:
    def __init__(self, idUsuario, idEmpleado, idRol, username, contrasena):
        self.idUsuario = idUsuario
        self.idEmpleado = idEmpleado
        self.idRol = idRol
        self.username = username
        self.contrasena = contrasena
#fdf
    def to_dict(self):
        return {
            "idUsuario": self.idUsuario,
            "idEmpleado": self.idEmpleado,
            "idRol": self.idRol,
            "username": self.username,
            "contrasena": self.contrasena
        }
