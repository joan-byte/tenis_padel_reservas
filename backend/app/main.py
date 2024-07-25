from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:3000",  # Asegúrate de que este sea el origen correcto
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/administradores/", response_model=schemas.Administrador)
def create_administrador(admin: schemas.AdministradorCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_administrador_by_name(db, nombre=admin.nombre)
    if db_admin:
        raise HTTPException(status_code=400, detail="Nombre ya registrado")
    return crud.create_administrador(db=db, admin=admin)

@app.get("/administradores/", response_model=list[schemas.Administrador])
def read_administradores(db: Session = Depends(get_db)):
    return crud.get_administradores(db)

@app.get("/administradores/{admin_id}", response_model=schemas.Administrador)
def read_administrador(admin_id: int, db: Session = Depends(get_db)):
    db_admin = crud.get_administrador(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return db_admin

@app.put("/administradores/{admin_id}", response_model=schemas.Administrador)
def update_administrador(admin_id: int, admin: schemas.AdministradorCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_administrador(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return crud.update_administrador(db=db, admin=admin, admin_id=admin_id)

@app.delete("/administradores/{admin_id}", response_model=schemas.Administrador)
def delete_administrador(admin_id: int, db: Session = Depends(get_db)):
    db_admin = crud.get_administrador(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return crud.delete_administrador(db=db, admin_id=admin_id)