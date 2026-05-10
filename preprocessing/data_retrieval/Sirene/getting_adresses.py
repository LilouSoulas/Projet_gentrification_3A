import pandas as pd
import requests
from geopy.geocoders import BANFrance
from geopy.extra.rate_limiter import RateLimiter

df = pd.read_csv("etablissements_56.30Z_years.csv")
api_url = "https://data.geopf.fr/geocodage/search"


# Convert columns to string and fill NaNs with an empty string
df['adresse'] = (
    df['numero_voie'].fillna(0).astype(int).astype(str) + ' ' +
    df['type_voie'].fillna('').astype(str) + ' ' +
    df['libelle_voie'].fillna('').astype(str) + ' ' +
    df['code_postal'].fillna('').astype(str)
)

# Clean up extra spaces caused by empty fields
df['adresse'] = df['adresse'].str.replace(r'\s+', ' ', regex=True).str.strip()
df.drop(columns=['numero_voie', 'type_voie', 'libelle_voie', 'code_postal'], inplace=True)

df = df[df['annee'] == 2010]
print(df['adresse'].head())


df.to_csv("etablissements_56.30Z_2010.csv", index=False)