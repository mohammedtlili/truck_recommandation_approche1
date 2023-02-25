import enum
from pydantic import BaseModel, validate_arguments
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categorie(enum.Enum):
    utilitaire = "utilitaire"
    fourgon = "fourgon"
    porteur = "porteur"
    camionette = "camionette"

class Transport(BaseModel):
    __tablename__ = "Transport"
    nmbre_km : int
    temps_service : float
    categorie : Categorie
    prix = float

    class Config:  
        use_enum_values = True


class Marchandise(BaseModel):
    __tablename__ = "Marchandise"
    prix_min : float
    prix_max : float
    categorie: Categorie
    #nbre_objet: int
    #label: str
#
# class Marchandise(BaseModel):
#     nbre_objet: int
#     label: str
