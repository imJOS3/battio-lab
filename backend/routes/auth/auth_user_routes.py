from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.LoginRequest import LoginRequest
from database.db import get_db
from services.Usuario_service import UsuarioService

auth_user_routes = APIRouter(prefix="/auth", tags=["Auth"])

@auth_user_routes.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    servicio = UsuarioService(db)
    usuario = servicio.verificar_credenciales(data.username, data.password)

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {
        "message": "Inicio de sesión exitoso",
        "user": {
            "idUsuario": usuario.idUsuario,
            "username": usuario.username,
            "idEmpleado": usuario.idEmpleado,
            "idRol": usuario.idRol
        }
    }
