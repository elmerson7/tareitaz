from fastapi import FastAPI
from api import tasks
from api import users
from database import Base, engine
import models  # importa los modelos para que SQLAlchemy los registre

app = FastAPI(title="Mini Task Manager API")

# Crea las tablas (solo la primera vez, luego se ignora si ya existen)
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

app.include_router(users.router, prefix="/users", tags=["Users"])
