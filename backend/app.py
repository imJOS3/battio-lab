from flask import Flask
from flask_cors import CORS  # ✅ Agregado
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

# Importa tus rutas
from routes.employee_routes import employee_bp
from routes.user_routes import user_bp
from routes.role_routes import role_bp
from routes.auth_routes import auth_bp  # ✅ Asegúrate de que existe este archivo

load_dotenv()

app = Flask(__name__)

# Configuración de JWT
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "clave-secreta-default")  # puedes usar un valor por defecto
jwt = JWTManager(app)

# ✅ Habilitar CORS para permitir solicitudes desde el frontend (como Tkinter, etc.)
CORS(app)

# Registrar Blueprints (rutas)
app.register_blueprint(employee_bp)
app.register_blueprint(user_bp)
app.register_blueprint(role_bp)

# Aquí agregamos el prefijo '/auth' para las rutas de autenticación
app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route("/")
def index():
    return "Bienvenido a Battio Lab API"

if __name__ == "__main__":
    app.run(debug=True)
