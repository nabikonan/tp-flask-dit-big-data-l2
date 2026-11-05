-- Instructions :
-- 1. Créer la base `gestion_etudiants` avec CREATE DATABASE IF NOT EXISTS,
--    en utf8mb4 / utf8mb4_unicode_ci.
-- 2. Ne PAS créer les tables ici : elles sont générées par SQLAlchemy
--    (db.create_all()) à partir des modèles de app/models/.
-- 3. Exécuter ce fichier : mysql -u root -p < sql/schema.sql

CREATE DATABASE gestion_etudiants;
USE  gestion_etudiants;