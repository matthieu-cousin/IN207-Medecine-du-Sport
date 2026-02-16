import sqlite3
import pandas as pd
import os

# Liste de tes fichiers CSV (assure-toi qu'ils sont dans le même dossier)
files = {
    'ATHLETE': 'athletes_table.csv',
    'TEST_MEDICAL': 'tests_table.csv',
    'ENTRAINEMENT': 'entrainements_table.csv',
    'INDICATEUR_PHYSIO': 'indicateurs_physio_table.csv',
    'PASSER': 'suivi_tests_table.csv',
    'BLESSURE': 'blessures_table.csv'
}

def create_and_populate_db():
    # 1. Connexion à la base de données (crée le fichier s'il n'existe pas)
    conn = sqlite3.connect('sport_health.db')
    cursor = conn.cursor()
    
    # Activer le support des clés étrangères
    cursor.execute("PRAGMA foreign_keys = ON;")

    print("--- Création des tables ---")
    
    # 2. Définition du schéma (DDL)
    # On supprime les tables existantes pour réinitialiser proprement
    cursor.executescript('''
    DROP TABLE IF EXISTS BLESSURE;
    DROP TABLE IF EXISTS PASSER;
    DROP TABLE IF EXISTS ENTRAINEMENT;
    DROP TABLE IF EXISTS INDICATEUR_PHYSIO;
    DROP TABLE IF EXISTS TEST_MEDICAL;
    DROP TABLE IF EXISTS ATHLETE;

    CREATE TABLE ATHLETE (
        id_athlete INTEGER PRIMARY KEY,
        age INTEGER CHECK (age > 0),
        genre TEXT NOT NULL,
        sport TEXT NOT NULL,
        bmi REAL CHECK (bmi BETWEEN 10 AND 50)
    );

    CREATE TABLE TEST_MEDICAL (
        id_test INTEGER PRIMARY KEY,
        nom_test TEXT NOT NULL,
        categorie TEXT CHECK (categorie IN ('Musculaire', 'Biométrique'))
    );

    CREATE TABLE ENTRAINEMENT (
        id_session INTEGER,
        id_athlete INTEGER NOT NULL,
        date_seance DATE NOT NULL,
        duree_minutes INTEGER CHECK (duree_minutes > 0),
        rpe_session INTEGER CHECK (rpe_session BETWEEN 1 AND 10),
        charge_travail REAL,
        surface_jeu INTEGER,
        PRIMARY KEY (id_session, id_athlete),
        FOREIGN KEY (id_athlete) REFERENCES ATHLETE(id_athlete) ON DELETE CASCADE
    );

    CREATE TABLE INDICATEUR_PHYSIO (
        id_mesure INTEGER PRIMARY KEY AUTOINCREMENT,
        id_athlete INTEGER NOT NULL,
        date_mesure DATE NOT NULL,
        temperature_corps REAL CHECK (temperature_corps BETWEEN 30 AND 45),
        frequence_cardiaque INTEGER CHECK (frequence_cardiaque > 0),
        qualite_sommeil REAL,
        score_recup REAL,
        niveau_stress REAL,
        fatigue_index REAL,
        hrv_repos INTEGER CHECK (hrv_repos > 0),
        FOREIGN KEY (id_athlete) REFERENCES ATHLETE(id_athlete) ON DELETE CASCADE
    );

    CREATE TABLE PASSER (
        id_athlete INTEGER NOT NULL,
        id_test INTEGER NOT NULL,
        date_examen DATE NOT NULL,
        valeur_mesuree REAL,
        resultat TEXT,
        PRIMARY KEY (id_athlete, id_test, date_examen),
        FOREIGN KEY (id_athlete) REFERENCES ATHLETE(id_athlete) ON DELETE CASCADE,
        FOREIGN KEY (id_test) REFERENCES TEST_MEDICAL(id_test)
    );

    CREATE TABLE BLESSURE (
        id_athlete INTEGER NOT NULL,
        id_session INTEGER NOT NULL,
        type_incident INTEGER,
        PRIMARY KEY (id_athlete, id_session),
        FOREIGN KEY (id_athlete) REFERENCES ATHLETE(id_athlete) ON DELETE CASCADE
    );
    ''')

    print("--- Importation des données ---")

    # 3. Importation des fichiers CSV
    for table_name, csv_file in files.items():
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            # Insertion des données dans la table SQLite
            df.to_sql(table_name, conn, if_exists='append', index=False)
            print(f"Table {table_name} importée avec succès ({len(df)} lignes).")
        else:
            print(f"Erreur : Le fichier {csv_file} est introuvable.")

    conn.commit()
    conn.close()
    print("\nBase de données 'sport_health.db' créée avec succès !")

if __name__ == "__main__":
    create_and_populate_db()