import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Solar Power Prediction",
    page_icon="🌞",
    layout="wide"
)

model = joblib.load("rf.joblib")

st.markdown("""
<style>
header {
    z-index: 1000 !important;
    position: relative;
}

[data-testid="stToolbar"] {
    z-index: 1000 !important;
}

.stApp {
    background: url("https://images.unsplash.com/photo-1509391366360-2e959784a276");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main {
    background: rgba(0,0,0,0.1);
}

.fixed-title {
    position: fixed;
    top: 45px;
    left: 50%;
    transform: translateX(-50%);
    width: 70%;
    text-align: center;
    padding: 12px;
    font-size: 34px;
    font-weight: bold;
    color: #ffffff;
    background: rgba(0,0,0,0.35);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    z-index: 900;
}

.page-content {
    margin-top: 120px;
}

section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.45);
    backdrop-filter: blur(10px);
    width: 280px !important;
}

button[kind="header"] {
    z-index: 1000 !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-size: 20px;
}

.glass-card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 20px;
    color: white;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    max-width: 850px;
    margin: auto;
}

input {
    background-color: rgba(255,255,255,0.9) !important;
    color: black !important;
}

.result-box {
    background: rgba(0,0,0,0.7);
    padding: 25px;
    margin-top: 25px;
    border-radius: 15px;
    text-align: center;
    color: #00ffcc;
    font-size: 30px;
    font-weight: bold;
    box-shadow: 0 0 25px rgba(0,255,200,0.6);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="fixed-title">🌞 Solar Power Generation Prediction</div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🔆 Navigation")
    page = st.radio(
        "",
        ["🏠 Home", "📘 About", "⚡ Predict"],
        index=0
    )

st.markdown('<div class="page-content">', unsafe_allow_html=True)

if page == "🏠 Home":
    st.markdown("""
    <div class="glass-card">
        <h2>Welcome to Solar Power Prediction</h2>
        <p>
        This application predicts solar power generation using real weather conditions
        such as temperature, wind, humidity, visibility and pressure.
        </p>
        <p>
        ✔ Machine Learning (Random Forest)<br>
        ✔ Clean Professional UI<br>
        ✔ Real-time Prediction
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "📘 About":
    st.markdown("""
    <div class="glass-card">
        <h2>About This Project</h2>
        <p>
            This project focuses on predicting solar power generation using historical
            weather and environmental data. The main objective is to help understand how
            different weather parameters influence solar energy output.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "⚡ Predict":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("Enter Weather Parameters")

    distance_to_solar_noon = st.number_input("Distance to Solar Noon")
    temperature = st.number_input("Temperature")
    wind_direction = st.number_input("Wind Direction")
    wind_speed = st.number_input("Wind Speed")
    sky_cover = st.number_input("Sky Cover")
    visibility = st.number_input("Visibility")
    humidity = st.number_input("Humidity")
    avg_wind_speed = st.number_input("Average Wind Speed (Period)")
    avg_pressure = st.number_input("Average Pressure (Period)")

    if st.button("🔮 Predict Power"):
        input_data = np.array([[distance_to_solar_noon, temperature, wind_direction,
                                wind_speed, sky_cover, visibility,
                                humidity, avg_wind_speed, avg_pressure]])

        prediction = model.predict(input_data)

        st.markdown(
            f'<div class="result-box">⚡ Predicted Power: {prediction[0]:.2f} Units</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)



