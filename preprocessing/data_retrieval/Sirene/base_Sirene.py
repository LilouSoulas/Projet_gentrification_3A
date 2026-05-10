import requests
import time
import csv
import json
import pandas as pd

TOKEN = "5b8dfefc-027b-46bc-8dfe-fc027bd6bcd6"
API_URL = "https://api.insee.fr/api-sirene/3.11/siret"

headers = {
    "X-INSEE-Api-Key-Integration": f"{TOKEN}",
    
}


ape = '56.30Z'

query = f"periode(activitePrincipaleEtablissement:{ape}) AND codePostalEtablissement:75*"
date = "2025-01-01"


rows = 1000
curseur = '*'
total = None

with open(f"etablissements_{ape}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["siret", "payload_json"])

    while curseur:
        params = {
            "q": query,
            "date": date,
            "champs": "siret,enseigne1Etablissement,etatAdministratifEtablissement,activitePrincipaleEtablissement,codePostalEtablissement,trancheEffectifsEtablissement,coordonneeLambertAbscisseEtablissement,coordonneeLambertOrdonneeEtablissement,dateCreationEtablissement,denominationUsuelleEtablissement,libelleVoieEtablissement,numeroVoieEtablissement,typeVoieEtablissement,caractereEmployeurEtablissement",
            "nombre": rows,
            "curseur": curseur
        }

        response = requests.get(API_URL, headers=headers, params=params)

        if response.status_code != 200:
            print("Erreur:", response.status_code, response.text)
            break

        data = response.json()

        if total is None:
            total = data["header"]["total"]

        etablissements = data.get("etablissements", [])

        if not etablissements:
            print("no etablissement")
            break

        for e in etablissements:
            siret = e.get("siret")

            payload = dict(e)
            payload.pop("siret", None)

            writer.writerow([
                siret,
                json.dumps(payload, ensure_ascii=False)
            ])

        print(f"Récupérés: {len(etablissements)} / {total}")

        curseur = data["header"].get("curseurSuivant")

        time.sleep(0.2)

df_check = pd.read_csv(f"etablissements_{ape}.csv")
print("Terminé.", len(df_check), "établissements récupérés.")