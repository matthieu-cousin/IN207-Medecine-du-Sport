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

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Sélection (σ)** : Filtre les lignes selon une condition",text_alignment="center")
    st.latex(r"\sigma_{condition}(R)")  

    st.markdown("**Projection (π)** : Sélectionne certaines colonnes",text_alignment="center")
    st.latex(r"\pi_{attributs}(R)")

with col2:
    st.markdown("**Jointure (⋈)** : Combine deux tables sur un attribut commun",text_alignment="center")
    st.latex(r"R \bowtie S")

    st.markdown("**Division (÷)** : Sélectionne les lignes qui correspondent à tous les attributs du diviseur",text_alignment="center")
    st.latex(r"R \div S")

st.markdown("---")

# Exemples de requêtes en algèbre relationnelle
st.header("10 Requêtes en algèbre relationnelle",text_alignment="center")


st.subheader("Bloc 1 : Identification et Profilage")

st.markdown("**R1 : Quel(le)s sont les joueurs(euses) de basket étant en surpoids ? (bmi (= IMC) > 28)**")
st.latex(r"R_1 = \pi_{id\_athlete} ( \sigma_{bmi > 28 \land sport = 'Basketball'} (ATHLETE) )")

st.markdown("**R2 : Quels sont les sports étudiés ?**")
st.latex(r"R_2 = \pi_{sport} (ATHLETE)")


st.subheader("Bloc 2 : Analyse de l'Entraînement")

st.markdown("**R3 : Quelle est la liste des séances d'entrainement de l'athlète 150 avec leurs durées ?**")
st.latex(r"R_3 = \pi_{date\_seance, duree\_minutes} ( \sigma_{id\_athlete = 150} (ENTRAINEMENT) )")

st.markdown("**R4 : Quelle est la liste des séances d'entrainement à haute intensité ?**")
st.latex(r"R_4 = \sigma_{duree\_minutes > 90 \land rpe\_session > 8} (ENTRAINEMENT)")

st.markdown("**R5 : Quels athlètes ont pratiqué sur l'intégralité des surfaces de jeu répertoriées ?**")
st.latex(r"R_5 = \pi_{id\_athlete, surface\_jeu} (ENTRAINEMENT) \div \pi_{surface\_jeu} (ENTRAINEMENT)")


st.subheader("Bloc 3 : Monitoring Physiologique (Santé)")

st.markdown("**R6 : Quels sont les athlètes en état d'alerte ?**")
st.latex(r"R_6 = \pi_{id\_athlete} ( \sigma_{niveau\_stress > 0.8} (INDICATEUR\_PHYSIO) ) \cup \pi_{id\_athlete} ( \sigma_{qualite\_sommeil < 3} (INDICATEUR\_PHYSIO) )")


st.subheader("Bloc 4 : Analyse des Incidents (Blessures)")

st.markdown("**R7 : Quelles sont les surfaces de jeu à risque chez les femmes ?**")
st.latex(r"R_7 = \pi_{surface\_jeu} (\sigma_{genre = 'Female'} (ATHLETE) \bowtie ENTRAINEMENT \bowtie BLESSURE)")

st.markdown("**R8 : Quels athlètes ne se sont jamais blessés ?**")
st.latex(r"R_8 = \pi_{id\_athlete} (ATHLETE) - \pi_{id\_athlete} (ENTRAINEMENT \bowtie BLESSURE)")

st.markdown("**R9 : Pour chaque athlète blessé, quelle est la liste des athlètes du même sport ?**")
st.latex(r"R_9 = \pi_{A1.id\_athlete, A2.id\_athlete} ( \sigma_{A1.id\_athlete \neq A2.id\_athlete} ( (ATHLETE_{A1} \bowtie \pi_{id\_athlete}(ENTRAINEMENT \bowtie BLESSURE)) \bowtie_{sport} ATHLETE_{A2} ) )")


st.subheader("Bloc 5 : Conformité et Protocoles")

st.markdown("**R10 : Quels sont les athlètes ayant réalisé l'intégralité du protocole médical ?**")
st.latex(r"R_{10} = \pi_{id\_athlete, id\_test} (PASSER) \div \pi_{id\_test} (TEST\_MEDICAL)")


st.markdown("---")

st.success("✅ Le MLD définit la structure logique des données. L'algèbre relationnelle permet d'exprimer formellement les requêtes.")
