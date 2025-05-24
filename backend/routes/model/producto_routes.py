# routes/model/producto_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import ValidationError
from services.Producto_service import ProductoService
from schemas.Producto_schema import ProductoCreate, ProductoUpdate, ProductoOut
from database.db import get_db

producto_routes = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@producto_routes.post("/", response_model=ProductoOut, status_code=201)
def crear_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    service = ProductoService(db)
    nuevo_producto = service.crear_producto(data.dict())
    return ProductoOut.from_orm(nuevo_producto)

@producto_routes.get("/", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    service = ProductoService(db)
    productos = service.listar_productos()
    return [ProductoOut.from_orm(p) for p in productos]

@producto_routes.get("/{id_implemento}", response_model=ProductoOut)
def obtener_producto(id_implemento: int, db: Session = Depends(get_db)):
    service = ProductoService(db)
    producto = service.obtener_producto_por_id(id_implemento)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return ProductoOut.from_orm(producto)

@producto_routes.put("/{id_implemento}", response_model=ProductoOut)
def actualizar_producto(id_implemento: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    service = ProductoService(db)
    producto_actualizado = service.actualizar_producto(id_implemento, data.dict(exclude_unset=True))
    if not producto_actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return ProductoOut.from_orm(producto_actualizado)

@producto_routes.delete("/{id_implemento}")
def eliminar_producto(id_implemento: int, db: Session = Depends(get_db)):
    service = ProductoService(db)
    resultado = service.eliminar_producto(id_implemento)
    if not resultado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado correctamente"}
