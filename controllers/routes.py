from fastapi import APIRouter, Request, Depends

from models.input_model import Transport, Marchandise, Categorie
from service.tarification import calcul, read_api, create_Marchandise
import tensorflow as tf
import io
from database.database import engine, SessionLocal
import pandas as pd
import numpy as np
import torch
import Levenshtein
import schemas
from sqlalchemy.orm import Session
from PIL import Image
import cv2
import os
from pymongo import MongoClient

router = APIRouter()

def get_db():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client['tarification']


@router.get("/hello")
def hello():
    return "hello"

@router.post("/calcul")
def input_transport(request_body: Transport):
    return calcul(request_body)

@router.get("/calcul")
def output_transport(request_body: Transport):
    return calcul(request_body)

@router.post("/model")
async def predict(request: Request):
    raw = await request.json()
    tmp, m, nmbre_km, temps_service = str(raw["img"]), int(raw["model"]), float(raw["nmbre_km"]), float(raw["temps_service"])
    db = get_db()
    col1 = db["transport"]
    if m == 1:
        model = tf.keras.models.load_model('MobileNet_model_0.792.h5')
        img = cv2.imread(os.path.join("assets", tmp))
        img = cv2.resize(img, (224, 224)) 
        img = img.reshape(1, 224, 224, 3)
        classes = ['camionette', 'fourgon', 'porteur', 'utilitaire']
        res = str(classes[np.argmax(model.predict(img))])
    if m == 2:
        img_bytes = open(os.path.join("assets", tmp), "rb")
        img_bytes = img_bytes.read()
        img = Image.open(io.BytesIO(img_bytes))
        model = torch.hub.load('yolov5', model='custom', path='last2.pt', source='local', force_reload=True)
        model.eval()
        results = model([img])
        results.render()
        df = results.pandas().xyxy[0].name.value_counts()
        d = {}
        for i in range(len(df)):
            d[str(df.index[i])] = int(df.values[i])
        x = np.sum(list(d.values()))
        res = "camionette" if (x == 4 or any([Levenshtein.ratio("réfrigérateur", k)>0.8 for k in d.keys()])) else "fourgon" if x == 2 else "porteur" if x == 3 else "utilitaire"
    d1 = {"temps_service":temps_service, "nmbre_km":nmbre_km, "categorie":res}
    col1.insert_one(d1)
    prix = temps_service * nmbre_km
    prix_min = prix
    if res == "utilitaire":
        prix = (0.14435 * nmbre_km)+(temps_service*3.7)+((temps_service* 119.3) / 8.43)
        prix_min = (0.14435 * nmbre_km)+(temps_service*3.7)+((temps_service* 87.96) / 8.43)

    elif (res == "fourgon") or (res == "camionette"):
        prix = (0.23005 * nmbre_km)+(temps_service*3.7)+((temps_service* 201.03) / 8.43)
        prix_min = (0.23005 * nmbre_km)+(temps_service*3.7)+((temps_service* 138.35) / 8.43)

    elif (res == "porteur"):
        prix = (0.28505 * nmbre_km)+(temps_service*3.7)+((temps_service* 214.16) / 8.43)
        prix_min = (0.28505 * nmbre_km)+(temps_service*3.7)+((temps_service* 182.72) / 8.43)

    else:
        print("choix invalide")
    d2 = {"prix_min":prix_min,"prix_max":prix,"categorie":res}
    interval_prix = Marchandise(prix_min=(prix_min*1.6), prix_max=(prix*1.6), categorie=res)
    col2 = db["marchandise"]
    col2.insert_one(d2)
    return interval_prix

@router.post("/model1")
async def model1(request: Request):
    raw = await request.json()
    model = tf.keras.models.load_model('MobileNet_model_0.792.h5')
    img = cv2.imread(os.path.join("assets", str(raw["img"])))
    img = cv2.resize(img, (224, 224)) 
    img = img.reshape(1, 224, 224, 3)
    classes = ['camionette', 'fourgon', 'porteur', 'utilitaire']
    res = str(classes[np.argmax(model.predict(img))])
    return res


@router.post("/model2")
async def model2(request: Request):
    raw = await request.json()
    img_bytes = open(os.path.join("assets", str(raw["img"])), "rb")
    img_bytes = img_bytes.read()
    img = Image.open(io.BytesIO(img_bytes))
    model = torch.hub.load('yolov5', model='custom', path='last2.pt', source='local', force_reload=True)
    model.conf = 0.2
    model.eval()
    results = model([img])
    results.render()
    results.save()
    df = results.pandas().xyxy[0].name.value_counts()
    d = {}
    for i in range(len(df)):
        d[str(df.index[i])] = int(df.values[i])
    return d

