from flask import Flask
from routes.employee_routes import employee_bp
from routes.user_routes import user_bp
from routes.role_routes import role_bp

app = Flask(__name__)

# Registrar Blueprints (rutas)
app.register_blueprint(employee_bp)
app.register_blueprint(user_bp)
app.register_blueprint(role_bp)

@app.route("/")
def index():
    return "Bienvenido a Battio Lab API"

if __name__ == "__main__":
    app.run(debug=True)
