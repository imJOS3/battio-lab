# cliente.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

class Cliente(Base):
    __tablename__ = "clientes"

    idCliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(15), nullable=True)
    direccion = Column(String(255), nullable=True)
    fechaRegistro = Column(DateTime, default=datetime.utcnow)
    estado = Column(Boolean, default=True)  # true = activo, false = inactivo

    servicios = relationship("Servicio", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(idCliente={self.idCliente}, nombre={self.nombre}, apellido={self.apellido})>"
