# servicio.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.Empleado import Empleado
from database.db import Base

class Servicio(Base):
    __tablename__ = "servicios"

    idServicio = Column(Integer, primary_key=True, autoincrement=True)
    idCliente = Column(Integer, ForeignKey("clientes.idCliente"), nullable=False)
    idEmpleado = Column(Integer, ForeignKey("empleados.idEmpleado"), nullable=False)
    tipoServicio = Column(String(100), nullable=False)
    fechaIngreso = Column(DateTime, nullable=False)
    fechaEntrega = Column(DateTime, nullable=True)
    observaciones = Column(Text, nullable=True)

    cliente = relationship("Cliente", back_populates="servicios")
    empleado = relationship("Empleado", back_populates="servicios")

    def __repr__(self):
        return f"<Servicio(tipoServicio='{self.tipoServicio}', fechaIngreso='{self.fechaIngreso}')>"
