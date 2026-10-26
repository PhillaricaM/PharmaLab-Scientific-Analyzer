
import requests
import pandas as pd

# Define the compounds we want to study
compound_ids = [
    "CHEMBL25",
    "CHEMBL112",
    "CHEMBL521"
]

# Create an empty list to store compound records
compound_records = []

# Retrieve molecular properties for each compound
for compound_id in compound_ids:

    url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{compound_id}.json"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    properties = data.get("molecule_properties", {})

    compound_record = {
        "chembl_id": data.get("molecule_chembl_id"),
        "compound_name": data.get("pref_name"),
        "molecular_formula": properties.get("full_molformula"),
        "molecular_weight": properties.get("full_mwt"),
        "logp": properties.get("alogp"),
        "psa": properties.get("psa")
    }

    # Add each compound record to our list
    compound_records.append(compound_record)

if compound_records:
    # Convert the list of dictionaries into a DataFrame
    compound_df = pd.DataFrame(compound_records)

    # Convert molecular properties into numeric values
    compound_df["molecular_weight"] = pd.to_numeric(
        compound_df["molecular_weight"], errors="coerce"
    )

    compound_df["logp"] = pd.to_numeric(
        compound_df["logp"], errors="coerce"
    )

    compound_df["psa"] = pd.to_numeric(
        compound_df["psa"], errors="coerce"
    )

    # Inspect the data types of our compound properties
    print("\nCompound data types:")
    print(compound_df.dtypes)
    
    # Calculate the average polar surface area
    average_psa = compound_df["psa"].mean()

    # Display the average PSA
    print("\nAverage Polar Surface Area:")
    print(round(average_psa, 2))

    # Display the results
    print("\nPharmaLab Compound Comparison")
    print(compound_df)

    from pathlib import Path

    # Define the folder where results will be saved
    results_folder = Path("results")

    # Create the folder if it does not exist
    results_folder.mkdir(exist_ok=True)

    # Define the CSV file location
    output_file = results_folder / "compound_comparison.csv"

    # Export the DataFrame to CSV
    compound_df.to_csv(output_file, index=False)

    print("\nDataset exported successfully:")
    print(output_file)

else:
    print("No compound data was retrieved. Please check your compound IDs or network connection.")
