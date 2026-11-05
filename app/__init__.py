# ÉTAPE 4 – Création de l'application (sans Blueprint)
#
# Instructions :
# 1. Importer Flask et Config (config.py).
from flask import Flask

# 2. Créer l'objet application au niveau du module : app = Flask(__name__)


# 3. Charger la configuration : app.config.from_object(Config)


# 4. Importer db depuis .extensions et le lier à l'application : db.init_app(app)


# 5. Tout en bas du fichier (pour éviter les imports circulaires), importer
#    les routes et les modèles : from app import routes, models
app = Flask(__name__)
from app import routes, models

# 6. Dans `with app.app_context():`, appeler db.create_all() pour créer les
#    tables automatiquement.


