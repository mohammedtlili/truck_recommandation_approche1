#Importation des parties SQLAlchemy¶
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Création d'une URL de base de données pour SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./Tarification.db"

# Créer le SQLAlchemyengine: consiste à créer un "moteur" SQLAlchemy.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Créer une SessionLocalclasse : une fois que nous créons une instance de la SessionLocalclasse,
# cette instance sera la session de base de données réelle.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Créer une Baseclasse:
# Nous allons maintenant utiliser la fonction declarative_base()qui renvoie une classe.
Base = declarative_base()