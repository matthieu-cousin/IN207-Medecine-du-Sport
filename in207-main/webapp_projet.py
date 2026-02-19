"""
Application principale - Définition de la navigation
"""

import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Prédiction de blessures chez les athlètes - IN207",
    page_icon="🤕",
    layout="wide"
)

# Configuration de la navigation
pg = st.navigation([
    st.Page("pages_webapp/1_Accueil.py", title="Accueil", icon="🏠", default=True),
    st.Page("pages_webapp/2_MCD.py", title="MCD", icon="📊"),
    st.Page("pages_webapp/3_MLD.py", title="MLD", icon="📋"),
    st.Page("pages_webapp/4_DDL.py", title="DDL", icon="🔧"),
    st.Page("pages_webapp/5_Requetes.py", title="Requêtes", icon="🔍"),
    st.Page("pages_webapp/6_Analyse.py", title="Analyse", icon="📈")
])

pg.run()
