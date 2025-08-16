import math
import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data


st.title("Weather Forcast for The Next Days")

city = st.text_input("Enter a City ",value="Tokyo", key="city")
days = st.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the muber of days you want to forecast")
option = st.selectbox("Select a data to view", ("Tempurature", "Sky"))



match option:
    case "Tempurature":
        data = get_data(city, days, option)
        dates = data[0]
        tempuratures = data[1]

        st.subheader(f"Tempurature for the next {days} days in {city}")
        figure = px.line(x=dates[0:int(days)*8], y=tempuratures[0:int(days)*8], labels={"x": "Date", "y": "Tempuratrue (c)"})
        st.plotly_chart(figure)