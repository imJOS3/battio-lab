from pydantic import BaseModel, ConfigDict
from typing import Optional

class RolBase(BaseModel):
    nombreRol: str

class RolCreate(RolBase):
    pass

class RolUpdate(BaseModel):
    nombreRol: Optional[str] = None

class RolOut(RolBase):
    idRol: int
    model_config = ConfigDict(from_attributes=True)
