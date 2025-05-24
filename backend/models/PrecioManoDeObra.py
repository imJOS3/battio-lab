from sqlalchemy import Column, String, Float
from database.db import Base

class PrecioManoDeObra(Base):
    __tablename__ = "precios_mano_obra"

    tipoServicio = Column(String(100), primary_key=True)  # Asumo que es único y sirve como PK
    precioBase = Column(Float, nullable=False)

    def __repr__(self):
        return f"<PrecioManoDeObra(tipoServicio='{self.tipoServicio}', precioBase={self.precioBase})>"
