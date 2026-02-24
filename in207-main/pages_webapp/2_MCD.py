"""
Page 1 - Modèle Conceptuel de Données (MCD)
Présentation du problème métier et du schéma entité-association
"""

import streamlit as st

st.title("1️⃣ Modèle Conceptuel de Données (MCD)")

st.markdown("---")

# Section : Énoncé du problème métier
st.header("Énoncé du problème métier")

st.markdown("""
> **Contexte :**  
> Un organisme de formation de sportif semblable à l'INSEP souhaite prédire les blessures de leurs athlètes.
> Nos entités seront les athlètes, leurs entrainements, leurs blessures, certains indicateurs physionomiques et le suivi de tests médicaux. 

**Besoins identifiés :**
- Identifier les athlètes, les entrainements et les tests médicaux de manière unique.
- Permettre des recherches et des statistiques sur les blessures des athlètes.
""")

st.markdown("---")

# Section : Schéma entité-association
st.header("Schéma Entité-Association")

# Représentation textuelle du schéma E-A
st.subheader("Exemple d'entité : ATHLETE")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.markdown("""
    ```
    ┌─────────────────────────────────────┐
    │               ATHLETE               │
    ├─────────────────────────────────────┤
    │               #id_athlete           │
    │               age                   │
    │               genre                 │
    │               sport                 │
    |               bmi                   |
    └─────────────────────────────────────┘
    ```
    """)

st.markdown("""
**Légende :**
- `#` : identifiant (clé primaire)
- Les autres attributs sont des propriétés de l'entité
""")

st.markdown("---")

# Placeholder pour une image
st.subheader("📷 Schéma Entité-Association")

st.image("MCD-MLD/MCD.png", caption="Schéma E-A")

st.markdown("---")

st.success("✅ Le MCD est la première étape : on identifie les entités et leurs attributs sans se soucier de l'implémentation technique.")
