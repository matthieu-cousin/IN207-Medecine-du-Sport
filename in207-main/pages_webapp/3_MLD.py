"""
Page 2 - Modèle Logique de Données (MLD)
Description des tables et introduction à l'algèbre relationnelle
"""

import streamlit as st

st.title("2️⃣ Modèle Logique de Données (MLD)")

st.markdown("---")

# Section : Description des tables
st.header("Description des tables")

st.markdown("""
Le passage du MCD au MLD consiste à traduire les entités en **tables relationnelles**.
""")

st.subheader("Exemple pour une table : Athlete")

# Tableau décrivant la structure
st.markdown("""
| Attribut | Type | Contraintes |
|----------|------|-------------|
| `#id_athlete` | INTEGER | PRIMARY KEY |
| `age` | INTEGER | CHECK (age > 0) |
| `genre` | TEXT | NOT NULL |
| `sport` | TEXT | NOT NULL |
| `bmi` | REAL | - |
""")

st.markdown("""
**Remarques :**
- La clé primaire 🔑 `#id_athlete` identifie de manière unique chaque sportif.
- L'attribut `age` est strictement positif.       
- Les attributs `sport` et `genre` sont obligatoires (NOT NULL).
- L'attribut `bmi` est optionnel.
""")

st.markdown("---")

# Placeholder pour une image
st.subheader("📷 MLD")

st.image("MCD-MLD/MLD.png", caption="Modèle Logique de Données")

st.info("""
**Remarque :** La clé étrangère (représenté par 🔗 sur le MLD) fait référence à la clef primaire d'une autre table.
""")

st.markdown("---")

# Section : Algèbre relationnelle
st.header("Algèbre Relationnelle")

st.markdown("""
L'algèbre relationnelle est un langage formel pour manipuler les relations (tables).
Voici les opérateurs principaux que nous utiliserons :
""")

# Opérateurs de base
st.subheader("Opérateurs de base")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Sélection (σ)** : Filtre les lignes selon une condition")
    st.latex(r"\sigma_{condition}(R)")  

with col2:
    st.markdown("**Projection (π)** : Sélectionne certaines colonnes")
    st.latex(r"\pi_{attributs}(R)")

with col3:
    st.markdown("**Jointure (⋈)** : Combine deux tables sur un attribut commun")
    st.latex(r"R \bowtie S")

st.markdown("---")

# Exemples de requêtes en algèbre relationnelle
st.subheader("Exemples de requêtes")

st.markdown("**1. Sélectionner les étudiants de plus de 20 ans :**")
st.latex(r"\sigma_{age > 20}(Etudiant)")

st.markdown("**2. Afficher uniquement les noms et prénoms :**")
st.latex(r"\pi_{nom, prenom}(Etudiant)")

st.markdown("**3. Noms des étudiants de plus de 20 ans :**")
st.latex(r"\pi_{nom}(\sigma_{age > 20}(Etudiant))")

st.markdown("---")

st.success("✅ Le MLD définit la structure logique des données. L'algèbre relationnelle permet d'exprimer formellement les requêtes.")
