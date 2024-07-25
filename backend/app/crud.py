from sqlalchemy.orm import Session
from . import models, schemas

def get_administrador(db: Session, admin_id: int):
    return db.query(models.Administrador).filter(models.Administrador.id == admin_id).first()

def get_administrador_by_name(db: Session, nombre: str):
    return db.query(models.Administrador).filter(models.Administrador.nombre == nombre).first()

def get_administradores(db: Session):
    return db.query(models.Administrador).all()

def create_administrador(db: Session, admin: schemas.AdministradorCreate):
    db_admin = models.Administrador(nombre=admin.nombre, password=admin.password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def update_administrador(db: Session, admin: schemas.AdministradorCreate, admin_id: int):
    db_admin = db.query(models.Administrador).filter(models.Administrador.id == admin_id).first()
    if db_admin:
        db_admin.nombre = admin.nombre
        db_admin.password = admin.password
        db.commit()
        db.refresh(db_admin)
    return db_admin

def delete_administrador(db: Session, admin_id: int):
    db_admin = db.query(models.Administrador).filter(models.Administrador.id == admin_id).first()
    if db_admin:
        db.delete(db_admin)
        db.commit()
    return db_admin