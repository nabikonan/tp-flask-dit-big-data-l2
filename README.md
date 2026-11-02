# Gestion des étudiants – projet fil rouge Flask + MySQL

## Structure

```
gestion_etudiants/
├── run.py                 # point d'entrée
├── config.py              # configuration (lit .env)
├── requirements.txt
├── .env.example
├── sql/schema.sql         # création de la base MySQL
└── app/
    ├── __init__.py        # création de l'app Flask
    ├── extensions.py      # db = SQLAlchemy()
    ├── models/            # modèles (Etudiant)
    ├── routes.py          # toutes les routes (sans Blueprint)
    ├── templates/         # base.html, index.html, etudiants/
    └── static/            # css/, js/, img/
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Créer la base dans MySQL :

```bash
mysql -u root -p < sql/schema.sql
```

Adapter `.env` (utilisateur / mot de passe MySQL), puis lancer :

```bash
python run.py
```

Les tables sont créées automatiquement au démarrage.

## À compléter au fil du cours

- CRUD des étudiants (`app/routes.py` + templates `etudiants/`)
- Validation des formulaires, messages flash
- Nouveaux modèles (filières, notes…) et relations
- Migrations (Flask-Migrate), authentification
# tp-flask-dit-big-data-l2
