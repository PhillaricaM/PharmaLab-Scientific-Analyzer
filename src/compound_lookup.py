import pandas as pd

import requests

# ChEMBL API endpoint for searching molecules
url = "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json"

# Define the compound we want to search for
parameters = {
    "q": "aspirin",
    "limit": 5
}

# Send the API request
response = requests.get(
    url,
    params=parameters,
    timeout=15
)

# Check whether the request succeeded
response.raise_for_status()

# Convert the JSON response into Python data
data = response.json()

# Extract the list of molecules
molecules = data["molecules"]

# Display the results
print("ChEMBL Compound Search Results")

for molecule in molecules:
    print("ChEMBL ID:", molecule.get("molecule_chembl_id"))
    print("Preferred Name:", molecule.get("pref_name"))
    print("------------------------")
    
    
# Convert the molecule records into a DataFrame
df = pd.DataFrame(molecules)

# Display the dataset dimensions
print("\nDataset dimensions:")
print(df.shape)

# Display available column names
print("\nAvailable columns:")
print(df.columns.tolist())

# Select the compound information we need
compound_data = df[
    ["molecule_chembl_id", "pref_name"]
]

# Display the organized results
print("\nPharmaLab Compound DataFrame:")
print(compound_data)


# Check for missing compound information
print("\nMissing compound information:")
print(compound_data.isnull().sum())
