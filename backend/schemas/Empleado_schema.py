from pydantic import BaseModel, EmailStr,ConfigDict
from typing import Optional
from datetime import datetime

# ✔️ Para crear un nuevo empleado
class EmpleadoCreate(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
    numeroTel: Optional[str] = None
    direccion: Optional[str] = None

# ✔️ Para actualizar un empleado (campos opcionales)
class EmpleadoUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[EmailStr] = None
    numeroTel: Optional[str] = None
    direccion: Optional[str] = None
    fechaSalida: Optional[datetime] = None
    estado: Optional[bool] = None

# ✔️ Para devolver un empleado desde la API
class EmpleadoOut(BaseModel):
    idEmpleado: int
    nombre: str
    apellido: str
    correo: EmailStr
    numeroTel: Optional[str]
    direccion: Optional[str]
    fechaIngreso: datetime
    fechaSalida: Optional[datetime]
    estado: bool

    model_config = ConfigDict(from_attributes=True)
