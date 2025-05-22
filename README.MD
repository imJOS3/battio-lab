Battio Lab - Backend

Este es el backend de Battio Lab, una aplicación para la gestión de repuestos y mantenimiento de scooters eléctricas.

Tecnologías Utilizadas

Python 3

Flask (Framework web)

MySQL (Base de datos)

Flask-MySQL-Connector (Conexión con MySQL)

Flask-CORS (Para manejo de CORS)

Instalación y Configuración

1️ Clonar el repositorio

git clone https://github.com/tu-usuario/battio-lab-backend.git
cd battio-lab-backend

2️ Crear y activar entorno virtual (opcional pero recomendado)

python -m venv venv  # Crear el entorno virtual
source venv/bin/activate  # Activar en Linux/macOS
venv\Scripts\activate  # Activar en Windows

3️ Instalar dependencias

pip install -r requirements.txt

4️ Configurar la Base de Datos

Asegúrate de tener MySQL instalado y ejecutando. Luego, crea la base de datos:

CREATE DATABASE battiolab;

Configura las credenciales en app.py:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
app.config['MYSQL_DB'] = 'battiolab'

5️ Ejecutar el servidor

python app.py

El backend se iniciará en http://127.0.0.1:5000/

🛠 Endpoints Disponibles

Empleados

GET /empleados/ → Obtener lista de empleados.

POST /empleados/crear → Crear un nuevo empleado.

Body (JSON):

{
  "nombre": "Juan",
  "apellido": "Pérez",
  "correo": "juan@example.com",
  "numeroTel": "123456789",
  "direccion": "Calle Falsa 123",
  "fechaIngreso": "2024-03-30"
}

Usuarios

GET /usuarios/ → Obtener lista de usuarios.

POST /usuarios/crear → Crear un nuevo usuario.

Body (JSON):

{
  "nombre": "Admin",
  "correo": "admin@example.com",
  "contraseña": "secreta",
  "rol": "admin"
}

 Próximos Pasos

Implementar autenticación con JWT.

Crear módulos para la gestión de repuestos.

Crear el frontend del login.

Conectar el backend con la interfaz gráfica.

