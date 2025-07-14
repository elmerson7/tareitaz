from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud.users as crud
import schemas

router = APIRouter()

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Registro de usuario
@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crud.create_user(db, user)


# Login de usuario (sin JWT aún)
@router.post("/login", response_model=schemas.UserOut)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    auth_user = crud.authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return auth_user
