import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('rf.joblib')

st.title("🌞 Solar Power Generation Prediction")

st.write("Enter weather conditions to predict power generation")
st.divider()
# === User Inputs (EXACT CSV FEATURES) ===
distance_to_solar_noon = st.number_input("Distance to Solar Noon")
temperature = st.number_input("Temperature")
wind_direction = st.number_input("Wind Direction")
wind_speed = st.number_input("Wind Speed")
sky_cover = st.number_input("Sky Cover")
visibility = st.number_input("Visibility")
humidity = st.number_input("Humidity")
avg_wind_speed = st.number_input("Average Wind Speed (Period)")
avg_pressure = st.number_input("Average Pressure (Period)")

# === Prediction ===
if st.button("Predict Power"):
    input_data = np.array([[
        distance_to_solar_noon,
        temperature,
        wind_direction,
        wind_speed,
        sky_cover,
        visibility,
        humidity,
        avg_wind_speed,
        avg_pressure
    ]])

    prediction = model.predict(input_data)
    st.markdown(
        f"""
        <div class="pred-box">
            <h3>⚡ Predicted Power Generated</h3>
            <h2>{prediction[0]} Units</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.metric(label="Prediction Status", value="Success ✅")
    st.progress(100)
    st.balloons()

st.divider()
st.markdown(
    "<p style='text-align:center; font-size:12px;'>☀️ Solar Power Prediction App | Streamlit Deployment</p>",
    unsafe_allow_html=True
)


