from flask import Flask
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager  # Agrega esta línea

# Importa tus rutas
from routes.employee_routes import employee_bp
from routes.user_routes import user_bp
from routes.role_routes import role_bp
from routes.auth_routes import auth_bp  # Asegúrate de que este nombre es correcto

load_dotenv()

app = Flask(__name__)

# Configurar JWT
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")  # Usa una clave segura en .env
jwt = JWTManager(app)  # ¡IMPORTANTE! Debes inicializarlo aquí

# Registrar Blueprints (rutas)
app.register_blueprint(employee_bp)
app.register_blueprint(user_bp)
app.register_blueprint(role_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def index():
    return "Bienvenido a Battio Lab API"

if __name__ == "__main__":
    app.run(debug=True)
