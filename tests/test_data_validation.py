

import pandas as pd

from src.data_validation import (
    check_invalid_inhibition,
    check_negative_concentrations,
    check_missing_values,
    
)


def test_invalid_inhibition():
    # Create a small test dataset
    data = pd.DataFrame({
        "compound_id": ["CMPD-001", "CMPD-002"],
        "concentration_uM": [5.0, 10.0],
        "inhibition_percent": [50, 125]
    })

    # Run our validation function
    result = check_invalid_inhibition(data)

    # Verify that one invalid row was found
    assert len(result) == 1

    # Verify that the invalid value is 125
    assert result.iloc[0]["inhibition_percent"] == 125
    
    
def test_negative_concentrations():
    # Create experimental data
    data = pd.DataFrame({
        "compound_id": ["CMPD-001", "CMPD-002"],
        "concentration_uM": [5.0, -10.0],
        "inhibition_percent": [50, 75]
    })

    # Run the validation function
    result = check_negative_concentrations(data)

    # Verify that one invalid row was found
    assert len(result) == 1

    # Verify that the invalid concentration is -10.0
    assert result.iloc[0]["concentration_uM"] == -10.0


def test_missing_values():
    # Create data containing missing measurements
    data = pd.DataFrame({
        "compound_id": ["CMPD-001", "CMPD-002"],
        "concentration_uM": [5.0, None],
        "inhibition_percent": [50, None]
    })

    # Run the validation function
    result = check_missing_values(data)

    # Verify missing values in each column
    assert result["compound_id"] == 0
    assert result["concentration_uM"] == 1
    assert result["inhibition_percent"] == 1
