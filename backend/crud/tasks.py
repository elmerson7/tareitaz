from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate

# Crear una nueva tarea
def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Obtener todas las tareas de un usuario
def get_tasks_by_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

# Obtener una tarea específica por ID
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# Actualizar una tarea (por ID)
def update_task(db: Session, task_id: int, data: dict):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    for key, value in data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

# Eliminar una tarea
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
