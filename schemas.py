from enum import Enum
from pydantic import BaseModel

"""
Création des modèles Pydantic (schémas) qui seront utilisés lors de la lecture des données,
lors de leur retour depuis l'API
Créer des modèles /schémas Pydantic pour la creation/l'entrée
"""
class MarchandiseBase(BaseModel):
    #nbre_objet: int
    #label: str | None = None
    pass

class MarchandiseCreate(MarchandiseBase):
    pass

#Créer des modèles /schémas Pydantic pour la lecture/le retour
class Marchandise(MarchandiseBase):
    #id_marchandise: int
    prix_min: float
    prix_max: float

    class Config:     #Pydantic orm_modedira au modèle Pydantic de lire les données même si ce n'est pas un dict
        orm_mode = True

class Categorie_vihecule(str, Enum):
    utilitaire = "Utilitaire"
    camionnette = "Camionnette"
    fourgon = "Fourgon"
    porteur = "Porteur"


class Transport(BaseModel):
    Nombre_km: float
    temps_service: int
    prix: float
    categorie: Categorie_vihecule

class TransportBase(BaseModel):
    Nombre_km: float
    temps_service: int
    #prix: float  | None = None


class TransportCreate(TransportBase):
    pass


class Transport(TransportBase):
    id_transport: int

    class Config:
        orm_mode = True
