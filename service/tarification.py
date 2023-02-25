from re import M
from models.input_model import Transport, Marchandise, Categorie
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from database.database import engine, SessionLocal
import models
import tensorflow as tf
import schemas
import io
import pandas as pd
import numpy as np
import torch
from PIL import Image
import cv2
import os



# *********************************************
models.input_model.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# *****************************************************

Transport = []

def read_api(db: Session = Depends(get_db)):
    return db.query(models.Marchandise).all()
# *****************************************************

def create_Marchandise(m: Marchandise, db: Session):

    m_model = Marchandise(prix_min = m.prix_min, prix_max=m.prix_max)

    db.add(m_model)
    db.commit()
    db.refresh(m_model)
    return m


def create_Transport(Transport: Transport, db: Session = Depends(get_db)):

    Transport_model = models.Transport()
    Transport_model.nmbre_km = Transport.nmbre_km
    Transport_model.temps_service = Transport.temps_service
    Transport_model.categorie = Transport.categorie
    Transport_model.prix = Transport.prix

    db.add(Transport_model)
    db.commit()

    return Transport


def calcul(request_input: Transport) -> Marchandise:
    # prix = 0
    prix = request_input.temps_service * request_input.nmbre_km
    prix_min = prix
    if request_input.categorie == Categorie.utilitaire:
        prix = (0.14435 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 119.3) / 8.43)
        prix_min = (0.14435 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 87.96) / 8.43)

    elif (request_input.categorie == Categorie.fourgon) or (request_input.categorie == Categorie.camionette):
        prix = (0.23005 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 201.03) / 8.43)
        prix_min = (0.23005 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 138.35) / 8.43)

    elif (request_input.categorie == Categorie.porteur):
        prix = (0.28505 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 214.16) / 8.43)
        prix_min = (0.28505 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 182.72) / 8.43)

    else:
        print("choix invalide")

    interval_prix = Marchandise(prix_min=(prix_min*1.5), prix_max=(prix*1.5))

    return interval_prix

# **********************************************************

#
# def read_all_marchandise(db: Session = Depends(), marchandise: Marchandise):
#     return db.query(input_models.Marchandise).all()

