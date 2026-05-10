import pandas as pd
import os 

# Chemins et listes de fichiers
data_dir = 'data/Geocoded_dico'
geocoded_files = os.listdir(data_dir) 

print(geocoded_files)

final_bdds = [
    'data/etablissements_56.10C_years_with_addresses.csv', 
    'data/etablissements_56.30Z_years_with_addresses.csv',
    'data/etablissements_56.10B_years_with_addresses.csv',
    'data/etablissements_56.10A_years_with_addresses.csv'
]

# On s'assure que l'ordre des fichiers correspond bien aux BDDs cibles
for i, bdd_path in enumerate(final_bdds):
    print(f"Traitement de : {bdd_path}")
    
    # 1. Charger la BDD principale et le fichier de géocodage correspondant
    df_main = pd.read_csv(bdd_path)
    df_geo = pd.read_csv(os.path.join(data_dir, geocoded_files[i]))
    
    # 2. Garder uniquement les colonnes nécessaires pour le mapping
    # On évite les doublons de colonnes lors du merge
    df_geo_subset = df_geo[['siret', 'latitude', 'longitude']].drop_duplicates('siret')
    
    # 3. Faire la jointure (équivalent d'un VLOOKUP ou LEFT JOIN)
    df_final = pd.merge(df_main, df_geo_subset, on='siret', how='left')
    
    # 4. Sauvegarder
    output_name = bdd_path.replace('.csv', '_with_coordinates.csv')
    df_final.to_csv(output_name, index=False)
    print(f"Sauvegardé : {output_name}")
