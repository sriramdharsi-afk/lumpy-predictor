
import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("lumpy_model.pkl", "rb"))

st.title("Lumpy Skin Disease Risk Predictor")

st.write("Enter environmental conditions:")

lat = st.number_input("Latitude", value=-17.6)
lon = st.number_input("Longitude", value=18.6)
elevation = st.number_input("Elevation (m)", value=1100)
temp_avg = st.number_input("Average Temperature (°C)", value=24.0)
rainfall = st.number_input("Rainfall", value=1.5)
country_code = st.number_input("Country Code", value=6)

if st.button("Predict"):

    data = pd.DataFrame({
        "lat": [lat],
        "lon": [lon],
        "elevation": [elevation],
        "temp_avg": [temp_avg],
        "rainfall": [rainfall],
        "country_code": [country_code]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error(f"High risk of Lumpy Skin Disease ({probability:.2%})")
    else:
        st.success(f"Low risk of Lumpy Skin Disease ({probability:.2%})")
