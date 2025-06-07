import streamlit as st
import pandas as pd

st.set_page_config(page_title="Delivery Time Prediction", layout="wide", page_icon=":star:")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Info", ["About Me", "Prediction"])

if page == "About Me":
    import about_me
    about_me.show_about_me()
if page == "Prediction":
    import Prediction
    Prediction.show_prediction()
