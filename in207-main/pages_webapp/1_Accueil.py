"""
Page 1 - Accueil du cours IN207
"""

import streamlit as st

# Titre principal
st.title("Prédiction de blessures chez les athlètes - IN207",text_alignment="center")

st.markdown("---")

# Présentation du projet
st.header("Bienvenue !",text_alignment="center")

st.subheader("""Cette application vous accompagne dans la construction d'une base de données pour la prédiction de blessures chez les athlètes.
""",text_alignment="center")


st.markdown("---")

st.subheader("""
Voici les 4 étapes fondamentales de conception de la base de données :
""",text_alignment="center")

# Présentation des 4 étapes
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ Modèle Conceptuel de Données (MCD)")
    st.markdown("""
    - Analyse du problème métier
    - Identification des entités et associations
    - Schéma entité-association
    """)
    
    st.subheader("2️⃣ Modèle Logique de Données (MLD)")
    st.markdown("""
    - Traduction du MCD en tables
    - Définition des attributs et types
    - Clés primaires et étrangères
    - Introduction à l'algèbre relationnelle
    """)

with col2:
    st.subheader("3️⃣ Création et Peuplement (DDL)")
    st.markdown("""
    - Requêtes CREATE TABLE
    - Requêtes INSERT
    - Création de la base SQLite
    """)
    
    st.subheader("4️⃣ Requêtes SQL")
    st.markdown("""
    - Requêtes SELECT
    - Filtrage, projection, jointures
    - Correspondance avec l'algèbre relationnelle
    """)


st.markdown("---")

st.subheader("""
La dernière étape propose une analyse des données pour identifier les facteurs de risque de blessures :
""",text_alignment="center")

_, col3, _ = st.columns(3,vertical_alignment="center")
with col3:
    st.subheader("5️⃣ Analyse des données")
    st.markdown("""
        - Requêtes SQL pour extraire les données pertinentes
        - Visualisation des résultats
        - Interprétation des facteurs de risque
        """)

st.markdown("---")

st.info("👈 Utilisez le menu latéral pour naviguer entre les différentes étapes.")
