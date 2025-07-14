from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from utils import hash_password, verify_password


# Crear nuevo usuario
def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(username=user.username, password_hash=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Buscar usuario por username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


# Verificar login
def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
