from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from database.db import Base

class Producto(Base):
    __tablename__ = "productos"

    ID_Implemento = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(150), nullable=False)
    Descripcion = Column(String(255), nullable=True)
    Categoria = Column(String(100), nullable=False)
    Marca = Column(String(100), nullable=True)
    Cantidad_Disponible = Column(Integer, nullable=False, default=0)
    Estado = Column(Boolean, nullable=False, default=True)  # Asumí booleano para estado activo/inactivo
    Fecha_Adquisicion = Column(Date, nullable=True)
    Costo_Adquisicion = Column(Float, nullable=True)
    Fecha_Ultima_Inspeccion = Column(Date, nullable=True)
    StockMinimo = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Producto(Nombre='{self.Nombre}', Categoria='{self.Categoria}', Cantidad={self.Cantidad_Disponible})>"
