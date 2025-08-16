import streamlit as st
import pandas as pd
import plotly as pl

st.title("Weather Forcast for The Next Days")
names = ["frankfurt", "stockholm", "liverpoll", "berlin"]
city = st.selectbox("select: ", names, key="city")
days = st.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the muber of days you want to forecast")
option = st.selectbox("Select a data to view", ("Tempurature", "Sky"))

st.subheader(f"Tempurature for the next {days} days in {city}")
