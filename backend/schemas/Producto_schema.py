from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

class ProductoBase(BaseModel):
    Nombre: str
    Categoria: str
    Cantidad_Disponible: int
    Estado: bool = True
    StockMinimo: int

    Descripcion: Optional[str] = None
    Marca: Optional[str] = None
    Fecha_Adquisicion: Optional[date] = None
    Costo_Adquisicion: Optional[float] = None
    Fecha_Ultima_Inspeccion: Optional[date] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    Nombre: Optional[str] = None
    Categoria: Optional[str] = None
    Cantidad_Disponible: Optional[int] = None
    Estado: Optional[bool] = None
    StockMinimo: Optional[int] = None
    Descripcion: Optional[str] = None
    Marca: Optional[str] = None
    Fecha_Adquisicion: Optional[date] = None
    Costo_Adquisicion: Optional[float] = None
    Fecha_Ultima_Inspeccion: Optional[date] = None

class ProductoOut(ProductoBase):
    ID_Implemento: int
    model_config = ConfigDict(from_attributes=True)
