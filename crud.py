from fastapi import Depends
from sqlalchemy.orm import Session



import models, schemas, main


def get_marchandise(db: Session, id_marchandise: int):
    return db.query(models.Marchandise).filter(models.Marchandise.id == id_marchandise).first()

def read_all_marchandise(db: Session = Depends(main.get_db)):
    return db.query(models.Marchandise).all()



def create_marchandise(db: Session, marchandise: schemas.MarchandiseCreate()):
    db_marchandise = models.Marchandise(nbre_objet=marchandise.nbre_objet, label=marchandise.label)
    db.add(db_marchandise)
    db.commit()
    db.refresh(db_marchandise)

    return db_marchandise