
import requests

url = "https://www.ebi.ac.uk/chembl/api/data/status.json"

response = requests.get(url, timeout=15)

print("HTTP status:", response.status_code)

response.raise_for_status()

data = response.json()

print("ChEMBL API response:")
print(data)
