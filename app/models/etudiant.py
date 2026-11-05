# ÉTAPE 5 – Modèle Etudiant (table `etudiants`)
#
# Instructions :
# 1. Importer db depuis ..extensions et datetime depuis le module datetime.
# 2. Créer la classe Etudiant(db.Model) avec __tablename__ = "etudiants".
# 3. Déclarer les colonnes avec db.Column :
#    - id              : Integer, clé primaire
#    - nom             : String(100), obligatoire (nullable=False)
#    - prenom          : String(100), obligatoire
#    - email           : String(150), unique et obligatoire
#    - date_naissance  : Date, facultative
#    - created_at      : DateTime, valeur par défaut = datetime.utcnow
# 4. Ajouter une méthode __repr__ qui renvoie un texte lisible
#    (ex. : "<Etudiant Prénom Nom>").
# 5. Vérifier dans MySQL (SHOW TABLES; DESCRIBE etudiants;) que la table est
#    bien créée au premier lancement.

from app.extensions import db
from datetime import datetime

class Etudiant(db.Model):
    __tablename__ = "etudiants"
    id = db.Column(db.Integer, PRIMARY_KEY=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), UNIQUE=True, nullable=False)
    date_naissance = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        print(f"Etudiant {self.prenom}, {self.nom} enregistré avec succès.")