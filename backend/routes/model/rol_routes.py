from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.Rol_schema import RolCreate, RolUpdate, RolOut
from services.Rol_service import RolService
from database.db import get_db

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RolOut, status_code=201)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    service = RolService(db)
    nuevo_rol = service.crear_rol(rol.nombreRol)
    return nuevo_rol

@router.get("/", response_model=list[RolOut])
def listar_roles(db: Session = Depends(get_db)):
    service = RolService(db)
    return service.listar_roles()

@router.get("/{id_rol}", response_model=RolOut)
def obtener_rol(id_rol: int, db: Session = Depends(get_db)):
    service = RolService(db)
    rol = service.obtener_rol_por_id(id_rol)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.put("/{id_rol}", response_model=RolOut)
def actualizar_rol(id_rol: int, data: RolUpdate, db: Session = Depends(get_db)):
    service = RolService(db)
    rol_actualizado = service.actualizar_rol(id_rol, data.nombreRol)
    if not rol_actualizado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol_actualizado

@router.delete("/{id_rol}")
def eliminar_rol(id_rol: int, db: Session = Depends(get_db)):
    service = RolService(db)
    resultado = service.eliminar_rol(id_rol)
    if not resultado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"message": "Rol eliminado correctamente"}
