from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

class Empleado(Base):
    __tablename__ = "empleados"

    idEmpleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    numeroTel = Column(String(20), nullable=True)
    direccion = Column(String(255), nullable=True)
    fechaIngreso = Column(DateTime, default=datetime.utcnow)
    fechaSalida = Column(DateTime, nullable=True)
    estado = Column(Boolean, default=True)  # True = activo, False = inactivo

    servicios = relationship("Servicio", back_populates="empleado")
    usuarios = relationship("Usuario", back_populates="empleado")

    def __repr__(self):
        return f"<Empleado(idEmpleado={self.idEmpleado}, nombre={self.nombre}, apellido={self.apellido})>"
