import pandas as pd

# Load the provided dataset
file_path = '/Users/paramanandbhat/Downloads/energy consumption 2.csv'
energy_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(energy_data.head())

import matplotlib.pyplot as plt

# Convert the 'DATE' column to datetime and set it as the index
energy_data['DATE'] = pd.to_datetime(energy_data['DATE'], format='%m/%Y')
energy_data.set_index('DATE', inplace=True)

# Plot the data
plt.figure(figsize=(15, 6))
plt.plot(energy_data['ENERGY_INDEX'])
plt.title('Monthly Energy Consumption')
plt.xlabel('Date')
plt.ylabel('Energy Index')
plt.grid(True)
plt.show()

from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np

# Define the training data
train_data = energy_data['ENERGY_INDEX']

# Fit the Holt-Winters model
model = ExponentialSmoothing(train_data, seasonal='add', seasonal_periods=12, trend='add').fit()

# Forecast for the next 3 years (36 months)
forecast_periods = 36
forecast = model.forecast(forecast_periods)

# Create a time series for the forecast dates
forecast_dates = pd.date_range(start=train_data.index[-1], periods=forecast_periods + 1, freq='M')[1:]

# Combine the forecast with the dates
forecast_series = pd.Series(forecast, index=forecast_dates)

# Plot the original data and the forecast
plt.figure(figsize=(15, 6))
plt.plot(train_data, label='Historical Data')
plt.plot(forecast_series, label='Forecast', color='red')
plt.title('Energy Consumption Forecast')
plt.xlabel('Date')
plt.ylabel('Energy Index')
plt.legend()
plt.grid(True)
plt.show()

