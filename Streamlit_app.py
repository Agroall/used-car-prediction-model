import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import HistGradientBoostingRegressor


# Configuration
st.set_page_config(
    page_title="Used Car Price Predictor",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load external styles
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load model
model = joblib.load("https://github.com/Agroall/used-car-prediction-model/blob/main/Notebooks/new_model.joblib")

# Column mapping
columns = [
    "vehicleType",
    "yearOfRegistration",
    "gearbox",
    "horsepower",
    "kilometer",
    "fuelType",
    "brand",
    "notRepairedDamage",
    "adTimeLength"
]


# Title Section
st.markdown("<h1 style='text-align: center;'>🚗 Used Car Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Estimate the fair market value of a used car based on key features</p>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.write("")
    st.write("")
    st.write("")
    st.image("https://cdn-icons-png.flaticon.com/512/743/743922.png", width=100)
    st.markdown("### About this App")
    st.write("Use this tool to estimate the resale price of a car in Europe based on key features such as age, mileage, fuel type, and more.")
    st.markdown("---")
    st.markdown("Built by **Abatan Ayodeji (Agroall)**")

# Option Maps
vehicle_type_options = ['Coupe', 'SUV', 'Small Car', 'Sedan', 'Convertible', 'Bus', 'Station Wagon', 'Other']
vehicle_map = dict(zip(vehicle_type_options, range(len(vehicle_type_options))))

gearbox_options = ['Manual', 'Automatic']
gearbox_map = {'Manual': 0, 'Automatic': 1}

fueltype_options = ['Diesel', 'Petrol', 'Other', 'LPG', 'Hybrid', 'CNG', 'Electric']
fueltype_map = dict(zip(fueltype_options, range(len(fueltype_options))))

brand_options = ['Budget', 'Economy', 'Luxury']
brand_map = {'Budget': 2, 'Economy': 0, 'Luxury': 1}

damages_options = ['Yes', 'No']
damaged_map = {'Yes': 0, 'No': 1}


# Form Layout
with st.form("car_form"):
    st.markdown("### 🚘 Car Details")
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        vehicle_type = st.selectbox("Car Type", vehicle_type_options)
    with row1_col2:
        brand = st.selectbox("Brand Category", brand_options)

    st.markdown("### 🔧 Engine & Fuel Information")
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        horsepower = st.slider("Horsepower", 20, 1000, 100, step=10)
        gearbox = st.selectbox("Gearbox Type", gearbox_options)
    with row2_col2:
        kilometer = st.slider("Mileage (km)", 0, 300000, 50000, step=1000)
        fueltype = st.selectbox("Fuel Type", fueltype_options)

    st.markdown("### 📈 Market & Listing Info")
    row3_col1, row3_col2 = st.columns(2)
    with row3_col1:
        car_year_reg = st.slider("Car Age (years)", 0, 80, 5)
    with row3_col2:
        adlength = st.slider("Ad Duration (days)", 0.0, 400.0, 20.0, step=0.1)

    st.markdown("### 🛠️ Condition")
    damages = st.selectbox("Any Unrepaired Damage?", damages_options)

    submitted = st.form_submit_button("🚀 Predict Price")


if submitted:
        # Encode inputs
        input_data = np.array([
            vehicle_map[vehicle_type],
            car_year_reg,
            gearbox_map[gearbox],
            horsepower,
            kilometer,
            fueltype_map[fueltype],
            brand_map[brand],
            damaged_map[damages],
            adlength
        ])
        X = pd.DataFrame([input_data], columns=columns)

        # Make prediction
        prediction = model.predict(X)[0]
        prediction = np.exp(prediction)
        rounded_price = round(prediction, 2)

        # Display prediction
        st.success(f"💶 Estimated Selling Price: **€{rounded_price:,}** ± 400 Euros")


# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🔧 This project is for educational use only. Do not use for financial decisions.</p>", unsafe_allow_html=True)
