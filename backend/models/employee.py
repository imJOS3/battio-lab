class Employee:
    def __init__(self, idEmpleados, nombre, apellido, correo, numeroTel=None, direccion=None, fechaIngreso=None, fechaSalida=None, estado="Activo"):
        self.idEmpleados = idEmpleados
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.numeroTel = numeroTel
        self.direccion = direccion
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.estado = estado

    def to_dict(self):
        return {
            "idEmpleados": self.idEmpleados,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "numeroTel": self.numeroTel,
            "direccion": self.direccion,
            "fechaIngreso": self.fechaIngreso,
            "fechaSalida": self.fechaSalida,
            "estado": self.estado
        }
