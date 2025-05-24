from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import ValidationError
from services.Servicio_service import ServicioService
from schemas.Servicio_schema import ServicioCreate, ServicioUpdate, ServicioOut
from database.db import get_db

servicio_routes = APIRouter(prefix="/servicios", tags=["Servicios"])

@servicio_routes.post("/", response_model=ServicioOut, status_code=201)
def crear_servicio(data: ServicioCreate, db: Session = Depends(get_db)):
    service = ServicioService(db)
    nuevo = service.crear_servicio(
        id_cliente=data.idCliente,
        id_empleado=data.idEmpleado,
        tipo_servicio=data.tipoServicio,
        fecha_ingreso=data.fechaIngreso,
        fecha_entrega=data.fechaEntrega,
        observaciones=data.observaciones
    )
    return ServicioOut.from_orm(nuevo)

@servicio_routes.get("/", response_model=list[ServicioOut])
def listar_servicios(db: Session = Depends(get_db)):
    service = ServicioService(db)
    servicios = service.listar_servicios()
    return [ServicioOut.from_orm(s) for s in servicios]

@servicio_routes.get("/{id_servicio}", response_model=ServicioOut)
def obtener_servicio(id_servicio: int, db: Session = Depends(get_db)):
    service = ServicioService(db)
    servicio = service.obtener_servicio_por_id(id_servicio)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return ServicioOut.from_orm(servicio)

@servicio_routes.put("/{id_servicio}", response_model=ServicioOut)
def actualizar_servicio(id_servicio: int, data: ServicioUpdate, db: Session = Depends(get_db)):
    service = ServicioService(db)
    servicio = service.actualizar_servicio(id_servicio, **data.dict(exclude_none=True))
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return ServicioOut.from_orm(servicio)

@servicio_routes.delete("/{id_servicio}")
def eliminar_servicio(id_servicio: int, db: Session = Depends(get_db)):
    service = ServicioService(db)
    eliminado = service.eliminar_servicio(id_servicio)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"message": "Servicio eliminado exitosamente"}
