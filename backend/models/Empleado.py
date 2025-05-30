from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from database.db import Base

class Empleado(Base):
    __tablename__ = "empleados"

    idEmpleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    apellido = Column(String(45), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    numeroTel = Column(String(15), unique=True, nullable=True)
    direccion = Column(String(255), nullable=True)
    fechaIngreso = Column(Date, nullable=False)
    fechaSalida = Column(Date, nullable=True)
    estado = Column(Boolean, default=True)  # Campo extra para control lógico si lo deseas

    servicios = relationship("Servicio", back_populates="empleado")
    usuarios = relationship("Usuario", back_populates="empleado")

    def __repr__(self):
        return f"<Empleado(idEmpleados={self.idEmpleados}, nombre={self.nombre}, apellido={self.apellido})>"
