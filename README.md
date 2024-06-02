# used-car-price-prediction-model

This Streamlit app allows you to predict the price of a used car based on various features. It uses a pre-trained LightGBM model to make predictions.

**Getting Started**

1. **Prerequisites:**
    - Python 3.x
    - Streamlit (`pip install streamlit`)
    - NumPy (`pip install numpy`)
    - Pandas (`pip install pandas`)
    - scikit-learn (`pip install scikit-learn`)
    - LightGBM (`pip install lightgbm`)
    - Joblib (`pip install joblib`)

2. **Clone the repository:**

   ```bash
   git clone 
   cd Car-Price-Prediction-Streamlit
   ```

3. **Run the app:**

   ```bash
   streamlit run Streamlit_app.py
   ```

**Using the App**

1. Open your web browser and navigate to .
2. Select the car's features from the dropdown menus and sliders.
   - **Vehicle Type:** Choose the type of car (coupe, suv, etc.)
   - **Year of Registration:** Enter the car's year of registration.
   - **Gearbox:** Select automatic or manual transmission.
   - **Horsepower:** Enter the car's horsepower.
   - **Mileage:** Enter the car's mileage in kilometers.
   - **Fuel Type:** Choose the car's fuel type (diesel, gasoline, etc.)
   - **Brand:** Select the car's brand (Budget, Economic, Luxury).
   - **Unrepaired Damage:** Indicate if the car has any unrepaired damage.
   - **Ad Length:** Enter how long the car has been up for sale.
3. Click the "Predict car price" button to see the predicted price of the car.

**Model Information**

- The model used for prediction is a pre-trained LightGBM model saved as `car_price_LGBMRegressor_model.joblib`.
- The model was trained on a dataset of used car prices with various features.

**Disclaimer**

This is a basic example and the predicted prices might not be fully accurate. The accuracy can depend on various factors such as the quality of the training data and the specific car being evaluated.
