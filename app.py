import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")

st.title("Prediksi Pembelian")

# Input user
gender = st.selectbox("Gender", ["L", "P"])
kota = st.selectbox("Kota", ["Batang", "Kendal", "Pekalongan"])
produk = st.selectbox("Produk", ["Celana", "Dress", "Hijab", "Jaket", "Kaos", "Kemeja"])
metode = st.selectbox("Metode", ["COD", "Transfer", "E-Wallet"])

harga = st.number_input("Harga", value=10000)
hari = st.slider("Hari", 1, 31)
bulan = st.slider("Bulan", 1, 12)
hari_dalam_minggu = st.slider("Hari dalam minggu (0=Senin)", 0, 6)

if st.button("Prediksi"):
    data = pd.DataFrame([{
        'Gender': gender,
        'Kota': kota,
        'Produk': produk,
        'Metode': metode,
        'Harga': harga,
        'Hari': hari,
        'Bulan': bulan,
        'Hari_dalam_minggu': hari_dalam_minggu
    }])

    hasil = model.predict(data)[0]
    st.success(f"Hasil prediksi: {hasil}")