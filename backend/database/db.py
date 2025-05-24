from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from database.config import DATABASE_URL

# Crear el motor (engine) de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True, future=True)  
# echo=True para debug (muestra queries en consola), poner False en producción

# Crear clase base para modelos ORM
Base = declarative_base()

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Función para obtener sesión DB (útil para usar en tus servicios o endpoints)
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
