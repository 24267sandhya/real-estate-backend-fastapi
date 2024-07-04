# app/main.py
import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from app import models, schemas, crud
from app.database import engine, Base, get_db

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/add_new_locality", response_model=schemas.Locality)
def create_locality(locality: schemas.LocalityCreate, db: Session = Depends(get_db)):
    db_locality = crud.get_locality_by_name(db, name=locality.name)
    if db_locality:
        raise HTTPException(status_code=400, detail="Locality already registered")
    return crud.create_locality(db=db, locality=locality)

@app.post("/add_new_property", response_model=schemas.Property)
def create_property(property: schemas.PropertyCreate, db: Session = Depends(get_db)):
    return crud.create_property(db=db, property=property)

@app.get("/fetch_all_properties", response_model=list[schemas.Property])
def fetch_all_properties(locality_name: str, db: Session = Depends(get_db)):
    locality = crud.get_locality_by_name(db, name=locality_name)
    if not locality:
        raise HTTPException(status_code=404, detail="Locality not found")
    return crud.get_properties_by_locality(db=db, locality_id=locality.id)

@app.put("/update_property_details", response_model=schemas.Property)
def update_property(property_id: int, property: schemas.PropertyCreate, db: Session = Depends(get_db)):
    return crud.update_property(db=db, property_id=property_id, property=property)

@app.delete("/delete_property_record", response_model=schemas.Property)
def delete_property(property_id: int, db: Session = Depends(get_db)):
    return crud.delete_property(db=db, property_id=property_id)
