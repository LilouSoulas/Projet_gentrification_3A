import pandas as pd
import json
from datetime import datetime


"""df = pd.read_csv("etablissements.csv")
for index, row in df.head().iterrows():
    siret = row["siret"]
    payload = json.loads(row["payload_json"])
    print(f"SIRET: {siret}, Payload: {payload}")    
"""

ape_codes = ["56.10A", "56.10B", "56.10C", "56.30Z"]

MIN_YEAR = 2010
END_YEAR = 2025

for code in ape_codes:

    df = pd.read_csv(f"etablissements_{code}.csv")

    rows = []

    for _, row in df.iterrows():
        siret = row["siret"]

        payload = json.loads(row["payload_json"])

        adresse = payload.get("adresseEtablissement", {})

        creation_date = payload.get("dateCreationEtablissement")
        lamb_abscisse_value = adresse.get("coordonneeLambertAbscisseEtablissement")
        lamb_ordonnee_value = adresse.get("coordonneeLambertOrdonneeEtablissement")
        numero_voie_value = adresse.get("numeroVoieEtablissement")
        type_voie_value = adresse.get("typeVoieEtablissement")
        libelle_voie_value = adresse.get("libelleVoieEtablissement")
        code_postal_value = adresse.get("codePostalEtablissement")

        periodes = payload.get("periodesEtablissement", [])


        for p in periodes:
            debut = p.get("dateDebut")
            fin = p.get("dateFin")

            if not debut:
                continue

            debut_year = int(debut[:4]) if debut else None
            fin_year = int(fin[:4]) if fin else END_YEAR

            if debut_year is None:
                continue

            start_year = max(MIN_YEAR, debut_year)
            fin_year = min(END_YEAR, fin_year)

            for year in range(start_year, fin_year + 1):
                rows.append({
                        "siret": siret,
                        "annee": year,
                        "etat": p.get("etatAdministratifEtablissement"),
                        "creation_date": creation_date,
                        "ape": p.get("activitePrincipaleEtablissement"),
                        "enseigne": p.get("enseigne1Etablissement"),
                        "denomination": payload.get("denominationUsuelleEtablissement"),
                        "employeur": p.get("caractereEmployeurEtablissement"),
                        "numero_voie": numero_voie_value,
                        "type_voie": type_voie_value,
                        "libelle_voie": libelle_voie_value,
                        "code_postal": code_postal_value,
                        "lamb_abscisse": lamb_abscisse_value,
                        "lamb_ordonnee": lamb_ordonnee_value
                    })

    df_years = pd.DataFrame(rows)
    df_years.to_csv(f"etablissements_{code}_years.csv", index=False)
    
print("Processing completed.")