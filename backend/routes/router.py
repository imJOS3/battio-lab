from fastapi import APIRouter
from routes.model.cliente_routes import cliente_routes
from routes.model.Factura_routes import Factura_routes
from routes.model.precioManoDeObra_routes import precioManoDeObra_routes
from routes.model.producto_routes import producto_routes
from routes.model.rol_routes import router as rol_router
from routes.model.servicio_routes import servicio_routes
from routes.model.usuario_routes import usuario_routes
from routes.auth.auth_user_routes import auth_user_routes

router = APIRouter()

# ✅ Prefijo manual "/api" para cada ruta excepto auth
router.include_router(cliente_routes, prefix="/api")
router.include_router(Factura_routes, prefix="/api")
router.include_router(precioManoDeObra_routes, prefix="/api")
router.include_router(producto_routes, prefix="/api")
router.include_router(rol_router, prefix="/api")
router.include_router(servicio_routes, prefix="/api")
router.include_router(usuario_routes, prefix="/api")

# ❌ Sin prefijo "/api" para login
router.include_router(auth_user_routes)  # mantiene el /auth/login
