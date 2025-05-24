# routes/model/precioManoDeObra_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.PrecioManoDeObra_service import PrecioManoDeObraService
from schemas.PrecioManoDeObra_schema import (
    PrecioManoDeObraCreate,
    PrecioManoDeObraUpdate,
    PrecioManoDeObraOut,
)
from database.db import get_db

precioManoDeObra_routes = APIRouter(
    prefix="/precios-mano-obra",
    tags=["Precios Mano de Obra"]
)

@precioManoDeObra_routes.post("/", response_model=PrecioManoDeObraOut, status_code=201)
def crear_precio(data: PrecioManoDeObraCreate, db: Session = Depends(get_db)):
    service = PrecioManoDeObraService(db)
    nuevo_precio = service.crear_precio(data.dict())
    return PrecioManoDeObraOut.from_orm(nuevo_precio)

@precioManoDeObra_routes.get("/", response_model=list[PrecioManoDeObraOut])
def listar_precios(db: Session = Depends(get_db)):
    service = PrecioManoDeObraService(db)
    precios = service.listar_precios()
    return [PrecioManoDeObraOut.from_orm(p) for p in precios]

@precioManoDeObra_routes.get("/{tipoServicio}", response_model=PrecioManoDeObraOut)
def obtener_precio(tipoServicio: str, db: Session = Depends(get_db)):
    service = PrecioManoDeObraService(db)
    precio = service.obtener_precio_por_tipo(tipoServicio)
    if not precio:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return PrecioManoDeObraOut.from_orm(precio)

@precioManoDeObra_routes.put("/{tipoServicio}", response_model=PrecioManoDeObraOut)
def actualizar_precio(tipoServicio: str, data: PrecioManoDeObraUpdate, db: Session = Depends(get_db)):
    service = PrecioManoDeObraService(db)
    precio_actualizado = service.actualizar_precio(tipoServicio, data.dict(exclude_unset=True))
    if not precio_actualizado:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return PrecioManoDeObraOut.from_orm(precio_actualizado)

@precioManoDeObra_routes.delete("/{tipoServicio}")
def eliminar_precio(tipoServicio: str, db: Session = Depends(get_db)):
    service = PrecioManoDeObraService(db)
    resultado = service.eliminar_precio(tipoServicio)
    if not resultado:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return {"message": "Precio eliminado correctamente"}
