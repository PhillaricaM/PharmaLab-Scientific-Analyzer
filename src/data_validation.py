
def check_missing_values(data):
    missing_values = data.isnull().sum()
    return missing_values

def check_negative_concentrations(data):
    invalid_concentrations = data[data["concentration_uM"] < 0]
    return invalid_concentrations

def check_invalid_inhibition(data):
    invalid_inhibition = data[
        (data["inhibition_percent"] < 0) |
        (data["inhibition_percent"] > 100)
    ]
    return invalid_inhibition