"""
Page 3 - Création et Peuplement (DDL)
Requêtes CREATE TABLE et INSERT, création de la base SQLite
"""

import streamlit as st
import sqlite3
import os

st.title("3️⃣ Création et Peuplement (DDL)")

st.markdown("---")

# Chemin vers la base de données
DB_PATH = "dataset/sport_health.db"

# Section : Requêtes CREATE TABLE
st.header("Requêtes CREATE TABLE")

st.markdown("""
Le DDL (Data Definition Language) permet de définir la structure de la base de données.
""")

col1, col2, col3 = st.columns(3)

with col1:

    create_table_sql = """
    DROP TABLE IF EXISTS ATHLETE;

    CREATE TABLE ATHLETE (
        id_athlete INTEGER PRIMARY KEY,
        age INTEGER CHECK (age > 0),
        genre TEXT NOT NULL,
        sport TEXT NOT NULL,
        bmi REAL CHECK (bmi BETWEEN 10 AND 50)
    );
    """

    st.code(create_table_sql, language="sql")

    create_table_sql = """
    DROP TABLE IF EXISTS PASSER;

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
    """

    st.code(create_table_sql, language="sql")


with col2:

    create_table_sql = """
    DROP TABLE IF EXISTS INDICATEUR_PHYSIO;

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
    """

    st.code(create_table_sql, language="sql")

    create_table_sql = """
    DROP TABLE IF EXISTS TEST_MEDICAL;

    CREATE TABLE TEST_MEDICAL (
        id_test INTEGER PRIMARY KEY,
        nom_test TEXT NOT NULL,
        categorie TEXT CHECK (categorie IN ('Musculaire', 'Biométrique'))
    );
    """

    st.code(create_table_sql, language="sql")

with col3:

    create_table_sql = """
    DROP TABLE IF EXISTS ENTRAINEMENT;

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
    """

    st.code(create_table_sql, language="sql")

    create_table_sql = """
    DROP TABLE IF EXISTS BLESSURE;

    CREATE TABLE BLESSURE (
        id_athlete INTEGER NOT NULL,
        id_session INTEGER NOT NULL,
        type_incident INTEGER,
        PRIMARY KEY (id_athlete, id_session),
        FOREIGN KEY (id_athlete) REFERENCES ATHLETE(id_athlete) ON DELETE CASCADE
    );
    """

    st.code(create_table_sql, language="sql")

st.markdown("""
**Explications :**
- `CREATE TABLE` : crée une nouvelle table
- `DROP TABLE IF EXISTS EXISTS` : supprime la table si elle existe déjà
- `INTEGER PRIMARY KEY` : clé primaire auto-incrémentée en SQLite
- `TEXT NOT NULL` : chaîne de caractères obligatoire
- `CHECK` : contrainte de valeur
""")

st.markdown("---")

# Section : Requêtes INSERT
st.header("Requêtes INSERT")

st.markdown("""
Les requêtes INSERT permettent d'ajouter des données dans les tables.
""")

st.markdown(""" Dans notre cas, les données proviennent d'un Dataset récupéré sur Kaggle.com intitulé : "Multimodal Sports Injury Prediction Dataset".""")
st.link_button("Lien vers le Dataset","https://www.kaggle.com/datasets/anjalibhegam/multimodal-sports-injury-dataset")

st.markdown("""
Après avoir fragmenté le dataset complet en plusieurs fichier.csv qui conviennent à notre représentation en base de données, il nous suffit d'utiliser la bibliothèque sqlite3 pour ajouter nos données.
""")

insert = """
    import sqlite3
    import pandas as pd
    import os

    files = {
    'ATHLETE': 'athletes_table.csv',
    'TEST_MEDICAL': 'tests_table.csv',
    'ENTRAINEMENT': 'entrainements_table.csv',
    'INDICATEUR_PHYSIO': 'indicateurs_physio_table.csv',
    'PASSER': 'suivi_tests_table.csv',
    'BLESSURE': 'blessures_table.csv'
    }

    conn = sqlite3.connect('sport_health.db')
    cursor = conn.cursor()

    print("--- Importation des données ---")

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
    """

st.code(insert, language="python")

st.markdown("---")

# Afficher le contenu actuel de la base
st.subheader("Contenu de la table ATHLETE",text_alignment='center')

if os.path.exists(DB_PATH):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ATHLETE")
        rows = cursor.fetchall()
        conn.close()
        
        if rows:
            import pandas as pd
            df = pd.DataFrame(rows, columns=['id_athlete', 'age', 'genre', 'sport', 'bmi'])
            st.dataframe(df, width='stretch')
        else:
            st.info("La table Etudiant est vide.")
    except Exception as e:
        st.error(f"Erreur de lecture : {e}")

