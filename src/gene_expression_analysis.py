
from pathlib import Path

import pandas as pd


# Locate the PharmaLab project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Location of downloaded GDC files
DATA_DIR = PROJECT_ROOT / "data" / "gdc"


def load_gene_expression(file_path):
    """Load a GDC RNA-seq gene-expression TSV file."""

    dataframe = pd.read_csv(
        file_path,
        sep="\t",
        comment="#",
        low_memory=False
    )

    return dataframe


def inspect_gene_expression(dataframe):
    """Display basic information about a gene-expression dataset."""

    print("\nDataset Dimensions:")
    print(dataframe.shape)

    print("\nColumn Names:")
    print(dataframe.columns.tolist())

    print("\nFirst Five Rows:")
    print(dataframe.head())

    print("\nData Types:")
    print(dataframe.dtypes)
   
def analyze_cancer_genes(dataframe):
    """Explore expression of selected cancer-associated genes."""

    cancer_genes = [
        "BRCA1",
        "BRCA2",
        "TP53",
        "ERBB2",
        "MKI67"
    ]

    # Remove sequencing summary rows and missing gene names
    gene_data = dataframe[
        dataframe["gene_id"].str.startswith("ENSG", na=False)
        & dataframe["gene_name"].notna()
    ].copy()

    # Select cancer-associated genes
    selected_genes = gene_data[
        gene_data["gene_name"].isin(cancer_genes)
    ].copy()

    # Keep relevant scientific measurements
    selected_genes = selected_genes[
        [
            "gene_id",
            "gene_name",
            "gene_type",
            "unstranded",
            "tpm_unstranded"
        ]
    ]

    # Sort by expression level
    selected_genes = selected_genes.sort_values(
        by="tpm_unstranded",
        ascending=False
    )

    return selected_genes


def export_cancer_gene_results(dataframe):
    """Export selected cancer gene-expression results."""

    results_dir = PROJECT_ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    output_path = results_dir / "tcga_brca_gene_expression.csv"

    dataframe.to_csv(output_path, index=False)

    print(f"\nResults exported to: {output_path}")

    return output_path

if __name__ == "__main__":

    # Find downloaded RNA-seq datasets
    files = list(DATA_DIR.glob("*.tsv"))

    if not files:
        print("No gene-expression files found in data/gdc/")

    else:
        selected_file = files[0]

        print("Loading:", selected_file.name)

        expression_data = load_gene_expression(selected_file)

        inspect_gene_expression(expression_data)
        
        
        print("\nCancer-Associated Gene Expression:")

        cancer_results = analyze_cancer_genes(
            expression_data
        )

        print(cancer_results.to_string(index=False))
        
        export_cancer_gene_results(cancer_results)

