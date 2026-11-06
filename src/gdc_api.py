
import json
from pathlib import Path

import requests


# National Cancer Institute Genomic Data Commons API
GDC_API_URL = "https://api.gdc.cancer.gov"

# PharmaLab project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Directory for downloaded gene-expression datasets
DATA_DIR = PROJECT_ROOT / "data" / "gdc"


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

    return response.json()["data"]["hits"]


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


def download_expression_file(file_id, file_name=None):
    """Download an open-access GDC gene-expression file."""

    endpoint = f"{GDC_API_URL}/data/{file_id}"

    # Create the data directory if it doesn't exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Use the original filename when available
    filename = file_name or f"{file_id}.tsv"
    output_path = DATA_DIR / Path(filename).name

    print(f"Downloading: {filename}")

    # Stream the download to avoid loading it all into memory
    with requests.get(
        endpoint,
        stream=True,
        timeout=120
    ) as response:

        response.raise_for_status()

        # Write to a temporary file until download completes
        temporary_path = output_path.with_name(
            output_path.name + ".part"
        )

        try:
            with open(temporary_path, "wb") as output_file:
                for chunk in response.iter_content(
                    chunk_size=8192
                ):
                    if chunk:
                        output_file.write(chunk)

            temporary_path.replace(output_path)

        finally:
            temporary_path.unlink(missing_ok=True)

    print(f"Download successful: {output_path}")

    return output_path


if __name__ == "__main__":

    project_id = "TCGA-BRCA"

    print(f"Searching gene-expression files for {project_id}")

    files = get_gene_expression_files(project_id)

    print(f"Gene Expression Files Found: {len(files)}")

    for file in files:
        print("-" * 40)
        print("File ID:", file["file_id"])
        print("File Name:", file["file_name"])
        print("Data Type:", file["data_type"])

    # Download only the first file for initial analysis
    if files:
        print("\nStarting first gene-expression download...")

        selected_file = files[0]

        downloaded_file = download_expression_file(
            selected_file["file_id"],
            selected_file["file_name"]
        )

        print("\nDataset ready for analysis:")
        print(downloaded_file)

    else:
        print("No matching gene-expression files found.")




