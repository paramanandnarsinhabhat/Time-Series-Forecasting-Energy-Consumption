
# Time Series Forecasting for Energy Consumption

This project applies the Holt-Winters method to forecast energy consumption based on historical data. It uses the `statsmodels` library to implement the forecasting model, `pandas` for data manipulation, `numpy` for numerical calculations, and `matplotlib` for plotting the results.

## Project Structure

- `data/`: Contains the CSV file with the historical energy consumption data.
- `notebook/`: Jupyter notebooks for exploratory analysis and interactive experimentation.
- `scripts/`: Python scripts for executing the time series forecasting model.
- `myenv/`: A virtual environment directory for the project dependencies.
- `requirements.txt`: A list of Python package dependencies.

## Installation

To set up the project environment, follow these steps:

1. Clone the repository to your local machine.

2. Navigate to the project directory:

```bash
cd path_to_project
```

3. It is recommended to use a virtual environment to manage dependencies. If you don't have `virtualenv` installed, you can install it using pip:

```bash
pip install virtualenv
```

4. Create a new virtual environment:

```bash
virtualenv myenv
```

5. Activate the virtual environment:

- On macOS and Linux:

```bash
source myenv/bin/activate
```

- On Windows:

```bash
myenv\Scripts\activate
```

6. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the forecasting script, execute the following command:

```bash
python scripts/time_series_forecasting_energy_consumption.py
```

The script will perform the following steps:
- Load the historical energy consumption data.
- Split the data into training and testing sets.
- Fit the Holt-Winters model to the training data.
- Forecast energy consumption for the next 36 months.
- Plot the historical data along with the forecast.

## Plotting

The script will generate a plot that displays:
- Historical energy consumption (in blue).
- A 3-year forecast of energy consumption (in green).

Make sure you have `matplotlib` installed to view the plots.

## Data

The energy consumption data is stored in `data/energy consumption 2.csv`. The dataset should have a `DATE` column and an `ENERGY_INDEX` column representing the time series data.

## Requirements

This project depends on the following Python packages:
- `statsmodels`
- `numpy`
- `matplotlib`
- `pandas`

Ensure all dependencies are installed using the `requirements.txt` file as mentioned in the installation steps.

## License

This project is open-source and available under the [MIT License](LICENSE).
```


**Note:** The `path_to_project` should be replaced with the actual path to the project directory where the user clones or downloads the repository.