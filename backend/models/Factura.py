from sqlalchemy import Column, Integer, DateTime, Float, Boolean, ForeignKey
from datetime import datetime
from database.db import Base

class Factura(Base):
    __tablename__ = "facturas"

    idFactura = Column(Integer, primary_key=True, autoincrement=True)
    idServicio = Column(Integer, ForeignKey("servicios.idServicio"), nullable=False)  # Relación con servicios
    fechaFactura = Column(DateTime, default=datetime.utcnow, nullable=False)
    subtotalProductos = Column(Float, nullable=False)
    precioManoObra = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    estadoPago = Column(Boolean, default=False)  # False = no pagado, True = pagado

    

    def __repr__(self):
        return (f"<Factura(idFactura={self.idFactura}, idServicio={self.idServicio}, "
                f"fechaFactura={self.fechaFactura}, total={self.total}, estadoPago={self.estadoPago})>")
