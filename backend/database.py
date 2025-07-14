from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ruta a la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.sqlite"

# Configuración especial para SQLite (solo para evitar errores con múltiples hilos)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()
