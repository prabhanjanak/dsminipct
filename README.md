
# Weather Data Analysis and Prediction

This project is a data science application built using Streamlit. It displays historical weather data and predicts future weather trends for 40 Indian cities using dummy data.

## Features
- **City Selection:** Choose one of 40 Indian cities to analyze weather data.
- **Past Weather Data:** View past 30 days of weather statistics.
- **Future Weather Prediction:** Predict weather trends for the next 7 days using a simple statistical model.
- **Interactive Charts:** Visualize weather trends using dynamic charts.

## Setup and Usage

### Prerequisites
- Python 3.7 or higher
- Install required packages using `pip`.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd weather-data-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Access the app in your browser at `http://localhost:8501`.

### File Descriptions
- `app.py`: Main Streamlit application script.
- `weather_data_40_cities.json`: Dummy weather data for 40 Indian cities.
- `requirements.txt`: List of dependencies required for the project.

## Data Description
The JSON file `weather_data_40_cities.json` contains:
- **City Names**: Names of 40 Indian cities.
- **Weather Data**: 
  - `date`: Date of the data point.
  - `temperature`: Temperature in °C.
  - `humidity`: Humidity in %.
  - `rainfall`: Rainfall in mm.

## Features in Detail
1. **City Selection**
   - Users can select a city from a dropdown menu.
   - The app dynamically updates weather statistics and predictions.

2. **Past Data Visualization**
   - Displays a line chart for temperature trends over the past 30 days.

3. **Future Weather Prediction**
   - Predicts temperatures for the next 7 days using a rolling average method.
   - Visualized using a line chart.

4. **Interactive Buttons**
   - "Show Past Data" displays historical statistics.
   - "Predict Future Weather" generates predictions.

## Screenshots
Include screenshots here (if available) for better understanding.

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

---

© 2024 Weather Analysis Project
