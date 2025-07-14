from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud.tasks as crud
import schemas

router = APIRouter()

# Dependencia para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crear nueva tarea
@router.post("/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# Obtener todas las tareas de un usuario
@router.get("/user/{user_id}", response_model=list[schemas.TaskOut])
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks_by_user(db, user_id)


# Obtener tarea por ID
@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


# Actualizar tarea
@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, update_data: dict, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, update_data)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


# Eliminar tarea
@router.delete("/{task_id}", response_model=schemas.TaskOut)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task
