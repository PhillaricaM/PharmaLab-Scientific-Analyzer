# PharmaLab Scientific Analyzer

**A Python Scientific Data Analysis Project for Pharmaceutical Research and Drug Discovery**

## Overview

PharmaLab Scientific Analyzer is a Python-based scientific computing project designed to retrieve, process, validate, and analyze pharmaceutical compound data.

The project integrates the ChEMBL REST API to retrieve publicly available chemical and pharmaceutical information and uses Python libraries to compare molecular properties and generate structured datasets for scientific visualization.

The goal is to develop practical scientific software engineering skills while exploring computational methods used in pharmaceutical and biotechnology research.

## Technologies

- Python 3.13
- pandas
- requests
- pytest
- ChEMBL REST API
- Tableau
- Git and GitHub
- Visual Studio Code

## Current Features

- Retrieve pharmaceutical compound information from the ChEMBL database
- Extract molecular properties, including molecular formula, molecular weight, LogP, and polar surface area (PSA)
- Compare multiple pharmaceutical compounds
- Process and organize scientific data using pandas
- Validate experimental datasets for missing values, negative concentrations, and invalid inhibition percentages
- Export compound comparison results to CSV
- Visualize compound information using Tableau dashboards
- Run automated data validation tests using pytest

## Example Compound Analysis

The project currently includes analysis of three pharmaceutical compounds:

| Compound | ChEMBL ID |
|---|---|
| Aspirin | CHEMBL25 |
| Acetaminophen | CHEMBL112 |
| Ibuprofen | CHEMBL521 |

These compounds provide a practical dataset for exploring molecular properties and comparing pharmaceutical substances.

## Project Structure

```text
PharmaLab-Scientific-Analyzer/
├── src/
│   ├── chembl_api.py
│   ├── compare_compounds.py
│   ├── compound_lookup.py
│   ├── data_validation.py
│   ├── explore_data.py
│   └── molecular_properties.py
├── tests/
│   └── test_data_validation.py
├── data/
│   └── drug_response.csv
├── results/
│   └── compound_comparison.csv
├── Tableau dashboards/
├── main.py
├── requirements.txt
└── README.md
```

## Data Visualization

The project includes Tableau workbooks for exploring compound properties and presenting scientific analysis results.

Current visualizations include molecular weight comparisons and compound analysis summaries.

## Testing and Validation

PharmaLab includes automated tests to support data quality and reliability.

The validation module checks for missing values, negative concentration measurements, and inhibition percentages outside the expected range.

Tests are implemented using pytest.

## Future Development

Planned improvements include:

- Expand compound analysis to additional pharmaceutical molecules
- Introduce dose-response analysis and IC50 calculations
- Add more advanced scientific visualizations
- Develop a reusable scientific analysis workflow
- Explore machine learning for pharmaceutical compound analysis
- Investigate integration with OncoCompute, a C++ scientific computing project for cancer drug discovery

## Scientific Applications

PharmaLab is a portfolio and learning project exploring software development techniques relevant to:

- Pharmaceutical research
- Drug discovery
- Scientific data analysis
- Computational biology
- Biotechnology research

**Project Status:** Active Development

**Author:** PhillaricaM