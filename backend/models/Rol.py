from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Rol(Base):
    __tablename__ = "roles"

    idRol = Column(Integer, primary_key=True, autoincrement=True)
    nombreRol = Column(String(100), nullable=False, unique=True)

    usuarios = relationship("Usuario", back_populates="rol")

    def __repr__(self):
        return f"<Rol(nombreRol='{self.nombreRol}')>"
