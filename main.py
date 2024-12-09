import streamlit as st
import pandas as pd
import json
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Load weather data
with open("data.json", "r") as f:
    weather_data = json.load(f)

# Helper function to predict future temperatures
def predict_future_temperatures(last_temp):
    future_temps = [round(last_temp + random.uniform(-2, 2), 1) for _ in range(7)]
    dates = [(datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 8)]
    return pd.DataFrame({"Date": dates, "Predicted Temperature (°C)": future_temps})

# Streamlit interface
st.title("Weather Analysis for Indian Cities")

# City selection
city = st.selectbox("Select a City", options=list(weather_data.keys()))

# Display past weather statistics
if st.button("Show Past Data"):
    past_data = pd.DataFrame(weather_data[city])
    st.subheader(f"Past 30 Days Weather Data for {city}")
    st.dataframe(past_data)

    # Plot past data
    st.subheader("Temperature Trend")
    plt.figure(figsize=(10, 5))
    plt.plot(past_data["date"], past_data["temperature"], marker="o", label="Temperature (°C)")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend in {city}")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Display future predictions
if st.button("Predict Future Weather"):
    last_temp = weather_data[city][-1]["temperature"]
    predictions = predict_future_temperatures(last_temp)
    st.subheader(f"Future 7-Day Weather Prediction for {city}")
    st.dataframe(predictions)

    # Plot predictions
    st.subheader("Predicted Temperature Trend")
    plt.figure(figsize=(10, 5))
    plt.plot(predictions["Date"], predictions["Predicted Temperature (°C)"], marker="o", label="Predicted Temperature (°C)")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Predicted Temperature Trend in {city}")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

st.write("\n---\n### Powered by Data Science")
