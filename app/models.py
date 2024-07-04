# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Locality(Base):
    __tablename__ = "localities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    property_name = Column(String, index=True)
    owner_name = Column(String, index=True)
    locality_id = Column(Integer, ForeignKey("localities.id"))

    locality = relationship("Locality")
