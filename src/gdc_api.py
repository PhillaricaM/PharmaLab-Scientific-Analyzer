
import requests

GDC_API_URL = "https://api.gdc.cancer.gov"


def get_cancer_projects():
    """Retrieve cancer research projects from the GDC API."""

    endpoint = f"{GDC_API_URL}/projects"

    params = {
        "size": 10,
        "fields": "project_id,name",
        "format": "JSON"
    }

    response = requests.get(
        endpoint,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return data["data"]["hits"]



def get_project_details(project_id):
    """Retrieve information about a specific GDC project."""

    endpoint = f"{GDC_API_URL}/projects/{project_id}"

    response = requests.get(
        endpoint,
        params={"format": "JSON"},
        timeout=30
    )

    response.raise_for_status()

    return response.json()["data"]


def get_gene_expression_files(project_id):
    """Find open-access RNA-seq gene-expression files."""

    endpoint = f"{GDC_API_URL}/files"

    filters = {
        "op": "and",
        "content": [
            {
                "op": "=",
                "content": {
                    "field": "cases.project.project_id",
                    "value": [project_id]
                }
            },
            {
                "op": "=",
                "content": {
                    "field": "data_type",
                    "value": ["Gene Expression Quantification"]
                }
            },
            {
                "op": "=",
                "content": {
                    "field": "access",
                    "value": ["open"]
                }
            }
        ]
    }

    import json

    params = {
        "filters": json.dumps(filters),
        "fields": "file_id,file_name,data_type,experimental_strategy",
        "format": "JSON",
        "size": 5
    }

    response = requests.get(
        endpoint,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["data"]["hits"]


if __name__ == "__main__":
    files = get_gene_expression_files("TCGA-BRCA")

    print("Gene Expression Files Found:", len(files))

    for file in files:
        print("File ID:", file["file_id"])
        print("File Name:", file["file_name"])
        print("Data Type:", file["data_type"])
        print("-" * 40)
    print("-" * 40)
    
    



