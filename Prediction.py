import joblib
import streamlit as st
import pandas as pd

def show_prediction():
    # Load dataset
    df = pd.read_csv('Food_Delivery_Times.csv', sep='\t')

    st.title("🚚 Prediksi Delivery Time")
    st.write("Masukkan detail pengiriman untuk memprediksi estimasi waktu pengiriman (dalam menit).")

    model = joblib.load("delivery_time_pipeline.pkl")
    # scaler = joblib.load("scaler1.pkl")

    with st.form("Prediction Form"):
        st.subheader("Please Input Your Data")

        distance = st.number_input("Jarak ke pelanggan (km)", min_value=0.0, step=0.1)
        prep_time = st.number_input("Waktu persiapan (menit)", min_value=0.0, step=1.0)
        courier_exp = st.slider("Pengalaman kurir (tahun)", min_value=0.0, max_value=9.0, step=1.0)
        weather = st.selectbox("Cuaca", ['Clear', 'Rainy', 'Foggy', 'Snowy', 'Windy'])
        traffic = st.selectbox("Tingkat Kemacetan", ['Low', 'Medium', 'High'])
        time_of_day = st.selectbox("Waktu Hari", ['Morning', 'Evening', 'Afternoon', 'Night'])
        vehicle = st.selectbox("Tipe Kendaraan", ['Bike', 'Scooter', 'Car'])

        submitted = st.form_submit_button("Predict")

    if submitted:
        input_df = pd.DataFrame([{
            'Distance_km': distance,
            'Preparation_Time_min': prep_time,
            'Courier_Experience_yrs': courier_exp,
            'Weather': weather,
            'Traffic_Level': traffic,
            'Time_of_Day': time_of_day,
            'Vehicle_Type': vehicle
        }])

        pred = model.predict(input_df)[0]
        st.success(f"⏱️ Estimasi waktu pengiriman: **{pred:.2f} Menit**")
