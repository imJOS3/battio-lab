from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.Empleado_service import EmpleadoService
from schemas.Empleado_schema import EmpleadoCreate, EmpleadoUpdate, EmpleadoOut
from database.db import get_db

empleado_routes = APIRouter(prefix="/empleados", tags=["Empleados"])

@empleado_routes.post("/", response_model=EmpleadoOut, status_code=201)
def crear_empleado(data: EmpleadoCreate, db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    nuevo_empleado = service.crear_empleado(data.dict())
    return EmpleadoOut.model_validate(nuevo_empleado)

@empleado_routes.get("/", response_model=list[EmpleadoOut])
def listar_empleados(db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    empleados = service.listar_empleados()
    return [EmpleadoOut.model_validate(e) for e in empleados]

@empleado_routes.get("/{idEmpleado}", response_model=EmpleadoOut)
def obtener_empleado(idEmpleado: int, db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    empleado = service.obtener_empleado_por_id(idEmpleado)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return EmpleadoOut.model_validate(empleado)

@empleado_routes.put("/{idEmpleado}", response_model=EmpleadoOut)
def actualizar_empleado(idEmpleado: int, data: EmpleadoUpdate, db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    empleado_actualizado = service.actualizar_empleado(idEmpleado, data.dict(exclude_unset=True))
    if not empleado_actualizado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return EmpleadoOut.model_validate(empleado_actualizado)

@empleado_routes.delete("/{idEmpleado}")
def eliminar_empleado(idEmpleado: int, db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    resultado = service.eliminar_empleado(idEmpleado)
    if not resultado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"message": "Empleado eliminado correctamente"}
