import pandas as pd

from data_validation import check_missing_values

# Load the experimental dataset
data = pd.read_csv("data/drug_response.csv")

# Display the dataset
print("PharmaLab Experimental Data")
print(data)


# Display the first five rows
print("\nFirst five rows:")
print(data.head())

# Display the last five rows
print("\nLast five rows:")
print(data.tail())

# Display the dataset dimensions
print("\nDataset dimensions:")
print(data.shape)

# Display the column names
print("\nColumn names:")
print(data.columns)

# Display the data types
print("\nData types:")
print(data.dtypes)


# Check for missing values
print("\nMissing values:")
print(check_missing_values(data))


# Check for negative drug concentrations
invalid_concentrations = data[data["concentration_uM"] < 0]

print("\nInvalid concentrations:")
print(invalid_concentrations)


# Check inhibition percentages outside 0-100
invalid_inhibition = data[
    (data["inhibition_percent"] < 0) |
    (data["inhibition_percent"] > 100)
]

print("\nInvalid inhibition percentages:")
print(invalid_inhibition)
