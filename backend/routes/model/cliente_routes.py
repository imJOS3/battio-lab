from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models.Clientes import Cliente
from services.Cliente_service import ClienteService
from schemas.Cliente_schema import ClienteCreate, ClienteUpdate, ClienteOut
from database.db import get_db  

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente_in: ClienteCreate, db: Session = Depends(get_db)):
    service = ClienteService(db)
    cliente = service.crear_cliente(cliente_in.dict())
    return cliente

@router.get("/{idCliente}", response_model=ClienteOut)
def obtener_cliente(idCliente: int, db: Session = Depends(get_db)):
    service = ClienteService(db)
    cliente = service.obtener_cliente_por_id(idCliente)
    if not cliente or not cliente.estado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.get("/", response_model=List[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    service = ClienteService(db)
    clientes = service.listar_clientes()
    return clientes

@router.put("/{idCliente}", response_model=ClienteOut)
def actualizar_cliente(idCliente: int, cliente_in: ClienteUpdate, db: Session = Depends(get_db)):
    service = ClienteService(db)
    cliente_actualizado = service.actualizar_cliente(idCliente, cliente_in.dict(exclude_unset=True))
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_actualizado

@router.delete("/{idCliente}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(idCliente: int, db: Session = Depends(get_db)):
    service = ClienteService(db)
    eliminado = service.eliminar_cliente(idCliente)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return None

cliente_routes = router
