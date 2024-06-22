import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import HistGradientBoostingRegressor

model = joblib.load('new_model.joblib')
columns = ['vehicleType', 'yearOfRegistration', 'gearbox', 'horsepower', 'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'adTimeLength']


st.title('Used Car Price Prediction Model')

vehicle_type = st.selectbox('What kind of car is it?', ['coupe', 'suv', 'kleinwagen', 'limousine', 'cabrio', 'bus', 'kombi', 'andere', 'other'])
car_year_reg = st.slider('How old in years is the car?', 0, 80)
gearbox = st.selectbox('Automatic or Manual', ['manuell', 'automatik'])
horsepower = st.slider('Car Horsepower:', 0, 1600)
kilometer = st.slider('Car Mileage:', 0, 150000)
fueltype = st.selectbox('What kind of Fuel does the car use?', ['diesel', 'benzin', 'andere', 'lpg', 'hybrid', 'cng', 'elektro', 'other'])
brand = st.selectbox('Car price grade?', ['Budget', 'Economic', 'Luxury'])
damages = st.selectbox('Any unrepaired damage?', ['ja', 'nein'])
adlength = st.slider('How long in days has this car been up for sale?', 0.0000, 400.000, step=0.1)


vehicle_map = {'coupe': 0, 'suv': 1, 'kleinwagen': 2, 'limousine': 3, 'cabrio': 4, 'bus': 5, 'kombi': 6, 'andere': 7, 'other': 8}
gearbox_map = {'manuell': 0, 'automatik': 1}
fueltype_map = {'diesel': 0, 'benzin': 1, 'andere': 2, 'lpg': 3, 'hybrid': 4, 'cng': 5, 'elektro': 6, 'other': 7}
damaged_map = {'ja': 0, 'nein': 1}
brand_map = {'Economic': 0, 'Luxury': 1, 'Budget': 2}


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

