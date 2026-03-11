"""
Page 4 - Requêtes SQL
Requêtes SELECT avec correspondance algèbre relationnelle
"""

import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("4️⃣ Requêtes SQL")

st.markdown("---")

# Chemin vers la base de données
DB_PATH = "dataset/sport_health.db"


def executer_requete(sql):
    """Exécute une requête SQL et retourne un DataFrame"""
    if not os.path.exists(DB_PATH):
        return None
    
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query(sql, conn)
        return df
    except Exception as e:
        st.error(f"Erreur SQL : {e}")
        return None
    finally:
        conn.close()


# Vérifier si la base existe
if not os.path.exists(DB_PATH):
    st.warning("⚠️ La base de données n'existe pas. Veuillez d'abord la créer dans la page DDL.")
    st.stop()


st.header("Bloc 1 : Identification et Profilage")


st.subheader("**1) Quel(le)s sont les joueurs(euses) de basket étant en surpoids ? (bmi (= IMC) > 28)**")

sql1 = "SELECT * FROM ATHLETE WHERE sport = 'Basketball' AND bmi > 28;"

col1, col2 = st.columns(2)

with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"\pi_{id\_athlete} ( \sigma_{bmi > 28 \land sport = 'Basketball'} (ATHLETE) )")

with col2:
    st.subheader("SQL")
    st.code(sql1, language="sql")

st.subheader("Résultat")
df1 = executer_requete(sql1)
if df1 is not None:
    st.dataframe(df1, width='stretch')


st.subheader("**2) Quels sont les sports étudiés ?**")

sql2 = "SELECT DISTINCT sport FROM ATHLETE;"

col1, col2 = st.columns(2)

with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"\pi_{sport} (ATHLETE)")
with col2:
    st.subheader("SQL")
    st.code(sql2, language="sql")

st.subheader("Résultat")
df1 = executer_requete(sql2)
if df1 is not None:
    st.dataframe(df1, width='stretch')


st.subheader("**3) Quel est le nombre d'athlètes suivis par genre ?**")

sql3 = "SELECT genre, COUNT(*) FROM ATHLETE GROUP BY genre;"

st.subheader("SQL")
st.code(sql3, language="sql")

st.subheader("Résultat")
df1 = executer_requete(sql3)
if df1 is not None:
    st.dataframe(df1, width='stretch')



st.markdown("---")



st.header("Bloc 2 : Analyse de l'Entraînement")

st.subheader("**4) Quelle est la liste des séances d'entrainement de l'athlète 150 avec leurs durées ?**")

sql2 = "SELECT date_seance,duree_minutes FROM ENTRAINEMENT WHERE id_athlete = 150;"

col1, col2 = st.columns(2)

with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"\pi_{date\_seance, duree\_minutes} ( \sigma_{id\_athlete = 150} (ENTRAINEMENT) )")


with col2:
    st.subheader("SQL")
    st.code(sql2, language="sql")

st.subheader("Résultat")
df2 = executer_requete(sql2)
if df2 is not None:
    st.dataframe(df2, width='stretch')


st.subheader("**5) Quelle est la liste des séances d'entrainement à haute intensité ?**")

sql2 = "SELECT * FROM ENTRAINEMENT WHERE duree_minutes > 90 AND rpe_session > 8;"

col1, col2 = st.columns(2)

with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"\sigma_{duree\_minutes > 90 \land rpe\_session > 8} (ENTRAINEMENT)")

with col2:
    st.subheader("SQL")
    st.code(sql2, language="sql")

st.subheader("Résultat")
df2 = executer_requete(sql2)
if df2 is not None:
    st.dataframe(df2, width='stretch')


st.subheader("**6) Quelle est la charge totale cumulée pour chaque athlète ?**")

sql2 = "SELECT id_athlete, SUM(charge_travail) FROM ENTRAINEMENT GROUP BY id_athlete;"

st.subheader("SQL")
st.code(sql2, language="sql")

st.subheader("Résultat")
df2 = executer_requete(sql2)
if df2 is not None:
    st.dataframe(df2, width='stretch')


st.subheader("**7) Quels sont les sports dont la charge moyenne par séance dépasse les 670 ?**")


sql3 = "SELECT sport, AVG(charge_travail) FROM ATHLETE A JOIN ENTRAINEMENT E ON A.id_athlete = E.id_athlete GROUP BY sport HAVING AVG(charge_travail) > 670 ORDER BY AVG(charge_travail);"

st.subheader("SQL")
st.code(sql3, language="sql")

st.subheader("Résultat")
df1 = executer_requete(sql3)
if df1 is not None:
    st.dataframe(df1, width='stretch')


st.markdown("---")



st.header("Bloc 3 : Monitoring Physiologique (Santé)")


st.subheader("**8) Quels sont les athlètes en état d'alerte ?**")

sql2 = "SELECT id_athlete FROM INDICATEUR_PHYSIO WHERE niveau_stress > 0.8 UNION SELECT id_athlete FROM INDICATEUR_PHYSIO WHERE qualite_sommeil < 3;"

col1, col2 = st.columns(2)

with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"\pi_{id\_athlete} ( \sigma_{niveau\_stress > 0.8} (INDICATEUR\_PHYSIO) ) \cup \pi_{id\_athlete} ( \sigma_{qualite\_sommeil < 3} (INDICATEUR\_PHYSIO) )")


with col2:
    st.subheader("SQL")
    st.code(sql2, language="sql")

st.subheader("Résultat")
df2 = executer_requete(sql2)
if df2 is not None:
    st.dataframe(df2, width='stretch')


st.subheader("**9) Quelle est la variabilité cardiaque au repos (hrv) pour chacun des âges de la basse de données ?**")


sql3 = "SELECT age, AVG(hrv_repos) FROM ATHLETE A JOIN INDICATEUR_PHYSIO I ON A.id_athlete = I.id_athlete GROUP BY age;"

st.subheader("SQL")
st.code(sql3, language="sql")

st.subheader("Résultat")
df1 = executer_requete(sql3)
if df1 is not None:
    st.dataframe(df1, width='stretch')


st.subheader("**10) Quels sont les pics de température corporelle pour chaque athlète ?**")


sql3 = "SELECT id_athlete, MAX(temperature_corps) FROM INDICATEUR_PHYSIO GROUP BY id_athlete;"

st.subheader("SQL")
st.code(sql3, language="sql")

st.subheader("Résultat")
df1 = executer_requete(sql3)
if df1 is not None:
    st.dataframe(df1, width='stretch')


st.markdown("---")

st.header("Bloc 4 : Analyse des Incidents (Blessures)")

st.info("**Blessure =** douleur qui empêche de faire du sport pour une durée supérieure à 1 jour (correpond au type_incident = 2 dans ma table). ")

st.subheader("**11) Quel est le sport où les athlètes se blessent le plus ?**")

sql11 = """
SELECT DISTINCT A.sport, COUNT(*)
FROM ATHLETE A 
JOIN BLESSURE B ON A.id_athlete = B.id_athlete 
WHERE B.type_incident = 2
GROUP BY A.sport
ORDER BY COUNT(*) DESC;
"""

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"\pi_{sport, count(*)} ( \sigma_{type\_incident = 2} (ATHLETE \bowtie_{id\_athlete} BLESSURE) )")
with col2:
    st.subheader("SQL")
    st.code(sql11, language="sql")

st.subheader("Résultat")
df11 = executer_requete(sql11)
if df11 is not None:
    st.dataframe(df11, width='stretch')


st.subheader("**12) Quels athlètes ne se sont jamais blessés ?**")

sql12 = """
SELECT A.id_athlete FROM ATHLETE A
EXCEPT 
SELECT E.id_athlete FROM ENTRAINEMENT E 
JOIN BLESSURE B ON E.id_session = B.id_session AND E.id_athlete = B.id_athlete
WHERE B.type_incident = 2;
"""

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"R_{12} = \pi_{id\_athlete} (ATHLETE) - \pi_{id\_athlete} (ENTRAINEMENT \bowtie BLESSURE)")
with col2:
    st.subheader("SQL")
    st.code(sql12, language="sql")

st.subheader("Résultat")
df12 = executer_requete(sql12)
if df12 is not None:
    st.dataframe(df12, width='stretch')


st.subheader("**13) Quel est le nombre de blessures enregistrées par type de surface ?**")

sql13 = "SELECT surface_jeu, COUNT(*) FROM ENTRAINEMENT E JOIN BLESSURE B ON E.id_session = B.id_session AND E.id_athlete = B.id_athlete WHERE B.type_incident = 2 GROUP BY surface_jeu ORDER BY COUNT(*) DESC;"

st.subheader("SQL")
st.code(sql13, language="sql")

st.subheader("Résultat")
df13 = executer_requete(sql13)
if df13 is not None:
    st.dataframe(df13, width='stretch')

st.markdown("""
**Surface_jeu :** 
     0 = Herbe, 
     1 = Gazon synthétique, 
     2 = Parquet, 
     3 = Piste, 
     4 = Autre
""")


st.subheader("**14) Quels sont les athlètes récidivistes (ayant eu plus de 20 blessures) ?**")

sql14 = "SELECT E.id_athlete, COUNT(*) FROM ENTRAINEMENT E JOIN BLESSURE B ON E.id_session = B.id_session AND E.id_athlete = B.id_athlete WHERE B.type_incident = 2 GROUP BY E.id_athlete HAVING COUNT(*) > 20;"

st.subheader("SQL")
st.code(sql14, language="sql")

st.subheader("Résultat")
df14 = executer_requete(sql14)
if df14 is not None:
    st.dataframe(df14, width='stretch')


st.markdown("---")


st.header("Bloc 5 : Conformité et Protocoles (Division)")

st.subheader("**15) Quels athlètes possèdent à la fois des entraînements et des tests médicaux validés ?**")

sql15 = "SELECT id_athlete FROM ENTRAINEMENT INTERSECT SELECT id_athlete FROM PASSER;"

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"R_{15} = \pi_{id\_athlete} (ENTRAINEMENT) \cap \pi_{id\_athlete} (PASSER)")
with col2:
    st.subheader("SQL")
    st.code(sql15, language="sql")

st.subheader("Résultat")
df15 = executer_requete(sql15)
if df15 is not None:
    st.dataframe(df15, width='stretch')


st.subheader("**16) Quels sont les athlètes ayant passé tous les tests de la catégorie 'Cardio' ?**")

sql16 = """
SELECT A.id_athlete FROM ATHLETE A
WHERE NOT EXISTS (
    SELECT T.id_test FROM TEST_MEDICAL T WHERE T.categorie = 'Cardio'
    EXCEPT
    SELECT P.id_test FROM PASSER P WHERE P.id_athlete = A.id_athlete
);
"""

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"R_{16} = \pi_{id\_athlete, id\_test} (PASSER) \div \pi_{id\_test} ( \sigma_{categorie = 'Cardio'} (TEST\_MEDICAL) )")
with col2:
    st.subheader("SQL")
    st.code(sql16, language="sql")

st.subheader("Résultat")
df16 = executer_requete(sql16)
if df16 is not None:
    st.dataframe(df16, width='stretch')


st.subheader("**17) Quels sont les athlètes ayant réalisé l'intégralité du protocole médical ?**")

sql17 = """
SELECT A.id_athlete FROM ATHLETE A
WHERE NOT EXISTS (
    SELECT id_test FROM TEST_MEDICAL
    EXCEPT
    SELECT P.id_test FROM PASSER P WHERE P.id_athlete = A.id_athlete
);
"""

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"R_{17} = \pi_{id\_athlete, id\_test} (PASSER) \div \pi_{id\_test} (TEST\_MEDICAL)")
with col2:
    st.subheader("SQL")
    st.code(sql17, language="sql")

st.subheader("Résultat")
df17 = executer_requete(sql17)
if df17 is not None:
    st.dataframe(df17, width='stretch')


st.markdown("---")


st.header("Bloc 6 : Analyse Environnementale et Synthèse")

st.subheader("**18) Quels athlètes ont pratiqué sur l'intégralité des surfaces de jeu répertoriées ?**")

sql18 = """
SELECT A.id_athlete FROM ATHLETE A
WHERE NOT EXISTS (
    SELECT DISTINCT surface_jeu FROM ENTRAINEMENT
    EXCEPT
    SELECT E.surface_jeu FROM ENTRAINEMENT E WHERE E.id_athlete = A.id_athlete
);
"""

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"R_{18} = \pi_{id\_athlete, surface\_jeu} (ENTRAINEMENT) \div \pi_{surface\_jeu} (ENTRAINEMENT)")
with col2:
    st.subheader("SQL")
    st.code(sql18, language="sql")

st.subheader("Résultat")
df18 = executer_requete(sql18)
if df18 is not None:
    st.dataframe(df18, width='stretch')


st.subheader("**19) Quel est le niveau de stress moyen par type de sport ?**")

sql19 = "SELECT A.sport, AVG(I.niveau_stress) FROM ATHLETE A JOIN INDICATEUR_PHYSIO I ON A.id_athlete = I.id_athlete GROUP BY A.sport ORDER BY AVG(I.niveau_stress) DESC;"

st.subheader("SQL")
st.code(sql19, language="sql")

st.subheader("Résultat")
df19 = executer_requete(sql19)
if df19 is not None:
    st.dataframe(df19, width='stretch')


st.subheader("**20) Analyse de voisinage : Comparer chaque blessé aux autres athlètes du même sport.**")

sql20 = """
SELECT DISTINCT A1.id_athlete AS id_blesse, A2.id_athlete AS id_comparaison
FROM ATHLETE A1
JOIN ENTRAINEMENT E ON A1.id_athlete = E.id_athlete
JOIN BLESSURE B ON E.id_session = B.id_session
JOIN ATHLETE A2 ON A1.sport = A2.sport
WHERE A1.id_athlete <> A2.id_athlete;
"""

col1, col2 = st.columns(2)
with col1:
    st.subheader("Algèbre relationnelle")
    st.latex(r"R_{20} = \pi_{A1.id, A2.id} ( \sigma_{A1.id \neq A2.id} ( (ATHLETE_{A1} \bowtie \pi_{id}(ENT \bowtie BLE)) \bowtie_{sport} ATHLETE_{A2} ) )")
with col2:
    st.subheader("SQL")
    st.code(sql20, language="sql")

st.subheader("Résultat")
df20 = executer_requete(sql20)
if df20 is not None:
    st.dataframe(df20, width='stretch')