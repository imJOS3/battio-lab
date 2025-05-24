from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ServicioBase(BaseModel):
    idCliente: int
    idEmpleado: int
    tipoServicio: str
    fechaIngreso: datetime
    fechaEntrega: Optional[datetime] = None
    observaciones: Optional[str] = None

class ServicioCreate(ServicioBase):
    pass

class ServicioUpdate(BaseModel):
    idCliente: Optional[int] = None
    idEmpleado: Optional[int] = None
    tipoServicio: Optional[str] = None
    fechaIngreso: Optional[datetime] = None
    fechaEntrega: Optional[datetime] = None
    observaciones: Optional[str] = None

class ServicioOut(ServicioBase):
    idServicio: int

    model_config = ConfigDict(from_attributes=True)
