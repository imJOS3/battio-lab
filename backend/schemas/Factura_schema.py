from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class FacturaCreate(BaseModel):
    idServicio: int
    subtotalProductos: float
    precioManoObra: float
    total: float
    estadoPago: Optional[bool] = False

class FacturaUpdate(BaseModel):
    idServicio: Optional[int] = None
    subtotalProductos: Optional[float] = None
    precioManoObra: Optional[float] = None
    total: Optional[float] = None
    estadoPago: Optional[bool] = None

class FacturaOut(BaseModel):
    idFactura: int
    idServicio: int
    fechaFactura: datetime
    subtotalProductos: float
    precioManoObra: float
    total: float
    estadoPago: bool

    model_config = ConfigDict(from_attributes=True)
