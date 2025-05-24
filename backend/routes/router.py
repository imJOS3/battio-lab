from fastapi import APIRouter
from routes.model.cliente_routes import cliente_routes
from routes.model.Factura_routes import Factura_routes
from routes.model.precioManoDeObra_routes import precioManoDeObra_routes
from routes.model.producto_routes import producto_routes
from routes.model.rol_routes import router as rol_router
from routes.model.servicio_routes import servicio_routes
from routes.model.usuario_routes import usuario_routes

router = APIRouter()

router.include_router(cliente_routes)
router.include_router(Factura_routes)
router.include_router(precioManoDeObra_routes)
router.include_router(producto_routes)
router.include_router(rol_router)
router.include_router(servicio_routes)
router.include_router(usuario_routes)
