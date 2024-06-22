import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import HistGradientBoostingRegressor

model = joblib.load('new_model.joblib')
columns = ['vehicleType', 'yearOfRegistration', 'gearbox', 'horsepower', 'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'adTimeLength']


st.title('Used Car Price Prediction Model')

# User Input with English options and German Mapping

vehicle_type_options = ['Coupe', 'SUV', 'Small Car', 'Sedan', 'Convertible', 'Bus', 'Station Wagon', 'Other']
vehicle_map = {'Coupe': 0, 'SUV': 1, 'Small Car': 2, 'Sedan': 3, 'Convertible': 4, 'Bus': 5, 'Station Wagon': 6, 'Other': 7}
vehicle_type = st.selectbox('What kind of car is it?', vehicle_type_options)

car_year_reg = st.slider('How old in years is the car?', 0, 80)

gearbox_options = ['Manual', 'Automatic']
gearbox_map = {'Manual': 0, 'Automatic': 1}
gearbox = st.selectbox('Automatic or Manual', gearbox_options)

horsepower = st.slider('Car Horsepower:', 0, 1600)

kilometer = st.slider('Car Mileage:', 0, 150000)

fueltype_options = ['Diesel', 'Petrol', 'Other', 'LPG', 'Hybrid', 'CNG', 'Electric', 'Other']
fueltype_map = {'Diesel': 0, 'Petrol': 1, 'Other': 2, 'LPG': 3, 'Hybrid': 4, 'CNG': 5, 'Electric': 6, 'Other': 7}
fueltype = st.selectbox('What kind of Fuel does the car use?', fueltype_options)

brand_options = ['Budget', 'Economy', 'Luxury']
brand_map = {'Budget': 2, 'Economy': 0, 'Luxury': 1}  
brand = st.selectbox('Car price grade?', brand_options)

damages_options = ['Yes', 'No']
damaged_map = {'Yes': 0, 'No': 1}
damages = st.selectbox('Any unrepaired damage?', damages_options)

adlength = st.slider('How long in days has this car been up for sale?', 0.0000, 400.000, step=0.1)

# Convert user choice to German using the maps
vehicle_type = vehicle_map[vehicle_type]
gearbox = gearbox_map[gearbox]
fueltype = fueltype_map[fueltype]
damages = damaged_map[damages]
brand = brand_map[brand]


def convert_and_run_model():
    row = np.array([vehicle_type, car_year_reg, gearbox, horsepower, kilometer, fueltype, brand, damages, adlength])
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)[0]
    prediction = np.exp(prediction)
    st.success(f'The selling price of the car is estimated to be around {prediction} Euros +/- 400Euros.')


st.button('Predict car price', on_click=convert_and_run_model)

st.markdown('---')
st.markdown('This application was created by Abatan Ayodeji (Agroall).')
