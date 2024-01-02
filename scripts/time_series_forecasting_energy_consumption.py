import pandas as pd

# Load the provided dataset
file_path = '/Users/paramanandbhat/Downloads/energy consumption 2.csv'
energy_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(energy_data.head())

