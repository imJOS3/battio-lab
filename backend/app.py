from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.router import router  # debe ser un APIRouter, no blueprints
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Battio Lab API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o restringe si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(router)

@app.get("/")
def index():
    return {"mensaje": "Bienvenido a Battio Lab API"}

# Ejecutar con uvicorn (NO usar python app.py directamente)
# Terminal: uvicorn app:app --reload
