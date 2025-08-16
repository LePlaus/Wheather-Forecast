import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Weather Forcast for The Next Days")
names = ["frankfurt", "stockholm", "liverpoll", "berlin"]
names.sort()
city = st.selectbox("select: ", names, key="city")
days = st.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the muber of days you want to forecast")
option = st.selectbox("Select a data to view", ("Tempurature", "Sky"))

st.subheader(f"Tempurature for the next {days} days in {city}")

dates = ["1", "2","3","4","5","6"]
tempuraures = [6,2,1.5,3,7,2,5,9]
figure = px.line(x=dates[0:int(days)+1], y=tempuraures[0:int(days)+1], labels={"x": "Date", "y": "Tempuratrue (c)"})
st.plotly_chart(figure)