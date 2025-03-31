from flask import Flask
from database import db
from routes.empleados import empleados_bp
from routes.usuarios import usuarios_bp

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
app.config['MYSQL_DB'] = 'battiolab'

# Inicializar base de datos
db.init_app(app)

# Registrar rutas
app.register_blueprint(empleados_bp, url_prefix='/empleados')
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
