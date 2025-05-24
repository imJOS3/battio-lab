from pydantic import BaseModel, ConfigDict
from typing import Optional

class PrecioManoDeObraCreate(BaseModel):
    tipoServicio: str
    precioBase: float

class PrecioManoDeObraUpdate(BaseModel):
    precioBase: Optional[float] = None

class PrecioManoDeObraOut(BaseModel):
    tipoServicio: str
    precioBase: float
    model_config = ConfigDict(from_attributes=True)
    
