# routes/model/Factura_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Factura
from services.Factura_service import FacturaService
from schemas.Factura_schema import FacturaCreate, FacturaUpdate, FacturaOut
from database.db import get_db

Factura_routes = APIRouter(prefix="/facturas", tags=["Facturas"])

@Factura_routes.post("/", response_model=FacturaOut, status_code=201)
def crear_factura(data: FacturaCreate, db: Session = Depends(get_db)):
    service = FacturaService(db)
    nueva_factura = service.crear_factura(data.dict())
    return FacturaOut.from_orm(nueva_factura)

@Factura_routes.get("/", response_model=list[FacturaOut])
def listar_facturas(db: Session = Depends(get_db)):
    service = FacturaService(db)
    facturas = service.listar_facturas()
    return [FacturaOut.from_orm(f) for f in facturas]

@Factura_routes.get("/{idFactura}", response_model=FacturaOut)
def obtener_factura(idFactura: int, db: Session = Depends(get_db)):
    service = FacturaService(db)
    factura = service.obtener_factura_por_id(idFactura)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return FacturaOut.from_orm(factura)

@Factura_routes.put("/{idFactura}", response_model=FacturaOut)
def actualizar_factura(idFactura: int, data: FacturaUpdate, db: Session = Depends(get_db)):
    service = FacturaService(db)
    factura_actualizada = service.actualizar_factura(idFactura, data.dict(exclude_unset=True))
    if not factura_actualizada:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return FacturaOut.from_orm(factura_actualizada)

@Factura_routes.delete("/{idFactura}")
def eliminar_factura(idFactura: int, db: Session = Depends(get_db)):
    service = FacturaService(db)
    resultado = service.eliminar_factura(idFactura)
    if not resultado:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return {"message": "Factura eliminada correctamente"}
