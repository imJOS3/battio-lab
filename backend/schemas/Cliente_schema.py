from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
    telefono: str | None = None
    direccion: str | None = None

class ClienteUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    correo: EmailStr | None = None
    telefono: str | None = None
    direccion: str | None = None

class ClienteOut(ClienteCreate):
    idCliente: int
    fechaRegistro: datetime
    estado: bool

    model_config = ConfigDict(from_attributes=True)
