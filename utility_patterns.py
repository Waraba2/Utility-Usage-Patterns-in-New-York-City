"""
Name: Hamidou Ballo
"""
import pandas as pd
import numpy as np

import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt


from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error



# Load your dataset
LINK = ("Energy_and_Water_Data_Disclosure_for_Local_Law_84_2022__"
        "Data_for_Calendar_Year_2021__20231105.csv")
ENERGY_USE = "Electricity Use – Generated from Onsite Renewable Systems (kWh)"

data = pd.read_csv(LINK, parse_dates=["Submission Date"], index_col="Submission Date")

# Replace 'Not Available' with NaN and convert the column to numeric
data[ENERGY_USE] = pd.to_numeric(
    data[ENERGY_USE].replace('Not Available', np.nan), errors='coerce'
                                 )

# Drop NaN values (or you can use interpolation or other methods to fill these gaps)
data.dropna(subset=[ENERGY_USE], inplace=True)

# Resample the target column to a desired frequency, e.g., weekly
weekly_data = data[ENERGY_USE].resample('W').sum()


# Generating a summary statistics plot for the weekly aggregated data
plt.figure(figsize=(10, 6))
weekly_data.plot(title="Weekly Electricity Generated from Onsite Renewable Systems (kWh)")
plt.xlabel('Week')
plt.ylabel('Electricity (kWh)')
plt.grid(True)

# # Saving the plot as a PNG file
# plot_file_path = '/work/weekly_electricity_usage.png'
# plt.savefig(plot_file_path, format='png')
plt.show()
# plot_file_path


# Selecting relevant columns for mapping
map_data = data[['Latitude', 'Longitude', ENERGY_USE]].dropna()

# Converting DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame(
    map_data,
    geometry=gpd.points_from_xy(map_data['Longitude'], map_data['Latitude']),
    crs="EPSG:4326"  # WGS 84 latitude-longitude projection
)

# Convert to Web Mercator projection for mapping
gdf = gdf.to_crs(epsg=3857)

# Plotting
ax = gdf.plot(
    figsize=(10, 10),
    column=ENERGY_USE,
    cmap='viridis',
    markersize=50,
    alpha=0.6,
    legend=True,
    legend_kwds={'label': "Electricity Usage (kWh)"}
)
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

plt.title('Map of Electricity Usage in NYC')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#  #Saving the map plot as a PNG file
# map_plot_file_path = '/work/electricity_usage_map.png'
# plt.savefig(map_plot_file_path, format='png')
plt.show()
#map_plot_file_path


# Splitting the weekly data into training and testing sets (80% train, 20% test)
train_size = int(len(weekly_data) * 0.8)
y_train, y_test = weekly_data[:train_size], weekly_data[train_size:]

# Fitting an ARIMA model (choosing a simple order (1, 1, 1) for demonstration)
Instructor
| 12/18 at 9:37 pm
Grading comment:
simpler is generally better actually.  very rarely do the p and q values go > 3.

arima_model = ARIMA(y_train, order=(1, 1, 1))
arima_model_fit = arima_model.fit()

# Making predictions on the test set
y_pred = arima_model_fit.forecast(steps=len(y_test))

# Calculating the mean squared error for the predictions
mse = mean_squared_error(y_test, y_pred)
print(mse)

# Plotting the actual vs predicted values
plt.figure(figsize=(10, 6))
plt.plot(y_train.index, y_train, label='Training Data')
plt.plot(y_test.index, y_test, label='Actual Values')
plt.plot(y_test.index, y_pred, label='Predicted Values', color='red')
plt.title('ARIMA Model Performance: Actual vs Predicted Electricity Generation')
plt.xlabel('Date')
plt.ylabel('Electricity Generation (kWh)')
plt.legend()
plt.grid(True)

# #Saving the map plot as a PNG file
# map_plot_file_path = '/work/ARIMA_model.png'
# plt.savefig(map_plot_file_path, format='png')
plt.show()
