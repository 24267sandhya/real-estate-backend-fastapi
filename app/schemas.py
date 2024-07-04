# app/schemas.py
from pydantic import BaseModel

class LocalityBase(BaseModel):
    name: str

class LocalityCreate(LocalityBase):
    pass

class Locality(LocalityBase):
    id: int

    class Config:
        orm_mode = True

class PropertyBase(BaseModel):
    property_name: str
    owner_name: str
    locality_id: int

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int

    class Config:
        orm_mode = True
