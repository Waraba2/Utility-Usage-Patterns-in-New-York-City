# Utility-Usage-Patterns-in-New-York-City

This project examines the patterns of utility usage, specifically electricity generated from onsite renewable systems, in New York City. The analysis is performed using GeoPandas for geospatial data handling and ARIMA modeling for time series forecasting.

## Project Overview

The primary focus of this project is to analyze and visualize the distribution and trends of electricity usage across NYC, leveraging various data analysis and geospatial mapping techniques.

### Data and Tools

- **Data Source**: Energy and Water Data Disclosure for Local Law 84 (2021)
- **Tools Used**:
  - Pandas and NumPy for data manipulation
  - GeoPandas for geospatial data handling
  - Contextily for basemap integration
  - Matplotlib for data visualization
  - Statsmodels for ARIMA modeling
  - Scikit-learn for model evaluation

### Key Findings

1. **Weekly Electricity Generation**:

   - The data was resampled to a weekly frequency to observe the trends in electricity generation from onsite renewable systems.
   - A summary statistics plot was generated to visualize these trends.

2. **Geospatial Distribution**:

   - The geographic distribution of electricity usage was mapped using GeoPandas.
   - The map highlights the intensity of electricity generation across different locations in NYC.

3. **ARIMA Modeling**:
   - An ARIMA model was fitted to the weekly data to forecast future electricity generation.
   - The model's performance was evaluated using mean squared error, and the actual vs. predicted values were plotted.

### Conclusion

The project provides valuable insights into the patterns of electricity generation from onsite renewable systems in NYC. The geospatial analysis and time series forecasting offer a comprehensive view of utility usage trends, which can aid in future planning and optimization.

For a detailed analysis, refer to the [full report](./Utility_Usage_Paterns_New_York_slides.pdf).
