from pydantic import BaseModel

class AdministradorBase(BaseModel):
    nombre: str

class AdministradorCreate(AdministradorBase):
    password: str

class Administrador(AdministradorBase):
    id: int

    class Config:
        orm_mode = True