# Instructions :
# Importer ici chaque modèle (ex. : from .etudiant import Etudiant) pour que
# SQLAlchemy les connaisse avant l'appel à db.create_all().
# À chaque nouveau modèle ajouté au projet, ajouter son import ici.

from .etudiant import Etudiant
from app.extensions import db

db.create_all()