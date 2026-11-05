# ÉTAPES 6 à 11 – Routes de l'application (sans Blueprint)
#
# Préparation :
# - Importer render_template, request, redirect, url_for, flash (et abort)
#   depuis flask.
from flask import Flask, render_template, request, redirect, url_for, flash

# - Importer `app` et `db` depuis le package app (from app import app, db)
#   et Etudiant depuis app.models.
from app import app
from app.models.etudiant import Etudiant

# - Les routes se déclarent directement avec @app.route(...). Les noms
#   utilisés dans url_for sont simplement ceux des fonctions
#   (ex. : url_for("liste")).


#
# ── 6. Page d'accueil  (GET /)  fonction `index`
#    - Renvoyer render_template("index.html").
@app.route('/')
def index():
    return render_template('index.html')

#
# ── 7. READ – liste  (GET /etudiants)  fonction `liste`
#    - Récupérer tous les étudiants : Etudiant.query.order_by(Etudiant.nom).all()
#    - Les passer au template etudiants/liste.html.


#
# ── 8. READ – détail (GET /etudiants/<int:id>)  fonction `detail`
#    - Récupérer l'étudiant avec Etudiant.query.get_or_404(id).
#    - Le passer au template etudiants/detail.html.
#

# ── 9. CREATE (GET + POST /etudiants/nouveau)  fonction `creer`
#    - Déclarer methods=["GET", "POST"].
#    - GET  : afficher etudiants/formulaire.html (formulaire vide).
#    - POST : lire request.form, vérifier que nom/prénom/email sont remplis,
#             créer un objet Etudiant, db.session.add(...), db.session.commit().
#             Gérer l'email déjà utilisé (try/except + db.session.rollback()).
#             Afficher un message avec flash(), puis redirect vers la liste.
@app.route('/etudiants/nouveau', methods = ["GET", "POST"])
def creer():
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        email = request.form.get("email")
        date_naissance = request.form.get("date_naissance")
        etudiant = Etudiant()
        etudiant.nom = nom
        etudiant.prenom = prenom
        etudiant.email = email
        etudiant.date_naissance = date_naissance
    else:
        return render_template("etudiants/formulaire.html")


#
# ── 10. UPDATE (GET + POST /etudiants/<int:id>/modifier)  fonction `modifier`
#    - Récupérer l'étudiant (get_or_404).
#    - GET  : afficher le même formulaire, pré-rempli avec ses valeurs.
#    - POST : mettre à jour ses attributs, db.session.commit(), flash(),
#             redirect vers la liste.
#

# ── 11. DELETE (POST /etudiants/<int:id>/supprimer)  fonction `supprimer`
#    - Uniquement en POST (jamais en GET).
#    - Récupérer l'étudiant, db.session.delete(...), db.session.commit(),
#      flash(), redirect vers la liste.