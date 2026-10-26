import pandas as pd

import requests

# Select aspirin using its ChEMBL identifier
compound_id = "CHEMBL25"

# Build the molecule API URL
url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{compound_id}.json"

# Request the compound record
response = requests.get(url, timeout=15)
response.raise_for_status()

# Convert the JSON response into Python data
data = response.json()

# Extract molecular properties
properties = data["molecule_properties"]

# Display the results
print("PharmaLab Molecular Properties")
print("Compound ID:", data["molecule_chembl_id"])
print("Preferred Name:", data["pref_name"])
print("Molecular Formula:", properties["full_molformula"])
print("Molecular Weight:", properties["full_mwt"])


# Organize the molecular properties
compound_record = {
    "chembl_id": data["molecule_chembl_id"],
    "compound_name": data["pref_name"],
    "molecular_formula": properties["full_molformula"],
    "molecular_weight": properties["full_mwt"]
}

# Convert the dictionary into a DataFrame
compound_df = pd.DataFrame([compound_record])

# Display the organized data
print("\nPharmaLab Molecular Properties DataFrame:")
print(compound_df)
