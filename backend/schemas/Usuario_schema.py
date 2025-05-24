from pydantic import BaseModel, ConfigDict
from typing import Optional

class UsuarioBase(BaseModel):
    idEmpleado: int
    idRol: int
    username: str

class UsuarioCreate(UsuarioBase):
    password: str  # Para creación, se incluye el password

class UsuarioUpdate(BaseModel):
    idEmpleado: Optional[int] = None
    idRol: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None

class UsuarioOut(UsuarioBase):
    idUsuario: int
    
    model_config = ConfigDict(from_attributes=True)

