from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Usuario(Base):
    __tablename__ = "users"

    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    idEmpleado = Column(Integer, ForeignKey("empleados.idEmpleado"), nullable=False)
    idRol = Column(Integer, ForeignKey("roles.idRol"), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Considera almacenar hashes

    empleado = relationship("Empleado", back_populates="usuarios")
    rol = relationship("Rol", back_populates="usuarios")

    def __repr__(self):
        return f"<Usuario(username='{self.username}')>"
