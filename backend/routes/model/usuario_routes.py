from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.Usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioOut
from database.db import get_db
from services.Usuario_service import UsuarioService

usuario_routes = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@usuario_routes.post("/", response_model=UsuarioOut, status_code=201)
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = UsuarioService.crear_usuario(db, data.dict())
    return UsuarioOut.from_orm(nuevo_usuario)

@usuario_routes.get("/", response_model=list[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    servicio = UsuarioService(db)
    usuarios = servicio.obtener_usuarios()
    return usuarios

@usuario_routes.get("/{username}", response_model=UsuarioOut)
def obtener_usuario_por_username(username: str, db: Session = Depends(get_db)):
    usuario = UsuarioService.obtener_usuario_por_username(db, username)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioOut.from_orm(usuario)

@usuario_routes.put("/{id_usuario}", response_model=UsuarioOut)
def actualizar_usuario(id_usuario: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = UsuarioService.actualizar_usuario(db, id_usuario, data.dict(exclude_none=True))
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioOut.from_orm(usuario)

@usuario_routes.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    eliminado = UsuarioService.eliminar_usuario(db, id_usuario)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado exitosamente"}
