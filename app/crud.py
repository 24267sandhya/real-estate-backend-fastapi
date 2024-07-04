# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_locality_by_name(db: Session, name: str):
    return db.query(models.Locality).filter(models.Locality.name == name).first()

def create_locality(db: Session, locality: schemas.LocalityCreate):
    db_locality = models.Locality(name=locality.name)
    db.add(db_locality)
    db.commit()
    db.refresh(db_locality)
    return db_locality

def get_properties_by_locality(db: Session, locality_id: int):
    return db.query(models.Property).filter(models.Property.locality_id == locality_id).all()

def create_property(db: Session, property: schemas.PropertyCreate):
    db_property = models.Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def update_property(db: Session, property_id: int, property: schemas.PropertyCreate):
    db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
    db_property.property_name = property.property_name
    db_property.owner_name = property.owner_name
    db_property.locality_id = property.locality_id
    db.commit()
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
    db.delete(db_property)
    db.commit()
    return db_property
