# ÉTAPE 2 – Point d'entrée de l'application
#
# Instructions :
# 1. Importer l'objet `app` depuis le package `app` (from app import app).
# 2. Dans un bloc `if __name__ == "__main__":`, lancer le serveur de
#    développement avec app.run(debug=True).
# 3. Lancer ensuite avec : python run.py  (puis ouvrir http://127.0.0.1:5000)

from app import app
if __name__ == "__main__":
    app.run(debug=True)