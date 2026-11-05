# ÉTAPE 3 – Extensions Flask
#
# Instructions :
# 1. Importer SQLAlchemy depuis flask_sqlalchemy.
# 2. Créer UNE instance globale : db = SQLAlchemy()
#    (elle n'est pas encore liée à l'application : c'est create_app() qui
#    appellera db.init_app(app)).
# 3. Cette instance sera importée par les modèles et les routes, ce qui évite
#    les imports circulaires.
