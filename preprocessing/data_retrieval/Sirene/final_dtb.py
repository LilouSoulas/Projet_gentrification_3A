import pandas as pd

df_chomage = pd.read_csv('data/conjoncture/tx_chom.csv', sep=';')
df_PIB = pd.read_csv('data/conjoncture/tx_pib.csv', sep=';')


files = ['data/preprocess/etablissements_56.10A_years_with_addresses_with_coordinates.csv',
         'data/preprocess/etablissements_56.10B_years_with_addresses_with_coordinates.csv',
         'data/preprocess/etablissements_56.10C_years_with_addresses_with_coordinates.csv',
         'data/preprocess/etablissements_56.30Z_years_with_addresses_with_coordinates.csv']

    
df = pd.concat([pd.read_csv(file) for file in files])

df = df[df["annee"] >= 2010]


# on identifie les siret ayant au moins une année active
siret_actifs = (
    df[df["etat"] == "A"]
    .groupby("siret")
    .size()
    .index
)

# on filtre
df = df[df["siret"].isin(siret_actifs)]

df.drop(columns=["lamb_abscisse", "lamb_ordonnee"], inplace=True)

# 1. On définit un ordre de priorité pour l'état : 'A' (Ouvert) avant 'F' (Fermé)
# Cela garantit qu'en cas de doublon, 'F' sera en bas de la pile
df['etat'] = pd.Categorical(df['etat'], categories=['A', 'F'], ordered=True)

# 2. On trie par SIRET, par Année, puis par Etat
df = df.sort_values(by=['siret', 'annee', 'etat'])

# 3. On supprime les doublons (siret + annee) en gardant la dernière ligne
# Puisque c'est trié, si un 'F' existe pour cette année, c'est lui qui restera
df = df.drop_duplicates(subset=['siret', 'annee'], keep='last')

# 4. On repasse la colonne 'etat' en format texte simple si besoin
df['etat'] = df['etat'].astype(str)

import pandas as pd

# Exemple de données
# df_chomage = pd.DataFrame({'trimestre': ['2023-T1', '2023-T2', '2024-T1'], 'taux': [7.1, 7.3, 7.5]})

# 1. Extraire l'année (les 4 premiers caractères)
df_chomage['annee'] = df_chomage['Libellé'].str[:4].astype(int)
df_PIB['annee'] = df_PIB['Libellé']

# 2. Calculer la moyenne par année
# On obtient une Series avec l'année en index et la moyenne en valeur
chomage_annuel = df_chomage.groupby('annee')['Taux de chômage localisé par département - Paris'].mean()

# On utilise .map() qui va chercher la valeur correspondant à 'annee' dans chomage_annuel
df['taux_chomage_annuel'] = df['annee'].map(chomage_annuel)
df['taux_croissance_PIB_annuel'] = df['annee'].map(df_PIB.set_index('annee')['Taux de croissance annuelle du PIB réel par habitant'])
# Vérification
print(df[['siret', 'annee', 'taux_chomage_annuel', 'taux_croissance_PIB_annuel']].head())

df.to_csv("data/final_data/final_dtb.csv", index=False)
