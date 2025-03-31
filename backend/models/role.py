class Role:
    def __init__(self, idRol, nombreRol):
        self.idRol = idRol
        self.nombreRol = nombreRol

    def to_dict(self):
        return {
            "idRol": self.idRol,
            "nombreRol": self.nombreRol
        }
