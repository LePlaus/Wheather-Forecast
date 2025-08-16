import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for The Next Days")

city = st.text_input("Enter a City: ", key="city")
days = st.slider("Forecast Days:", max_value=5, min_value=1,
                 help="Select the muber of days you want to forecast.")
option = st.selectbox("Select a data to view", ("Tempurature", "Sky"))

if city:
    try:
        if option == "Tempurature":
            data = get_data(city, days, option)
            dates = data[0] #type:ignore

            tempuratures = data[1] #type:ignore 
            st.subheader(f"Tempurature for the next {days} days in {city}")
            figure = px.line(x=dates, y=tempuratures, labels={"x": "Date", "y": "Tempuratrue (c)"})
            st.plotly_chart(figure)


        else:
            
            data = get_data(city, days, option)
            dates = data[0] #type:ignore
            sky_status = data[1] #type:ignore
            sky_description = data[2] #type:ignore

            print(sky_status)
            image_dict = {"Clear": "images/clear.png", "Clouds":"images/cloud.png",
                        "Rain": "images/rain.png", "Snow": "images/snow.png"}
            images = [image_dict[condition] for condition in sky_status]
            captions = []
            for index, dt in enumerate(dates):
                dt = f"{sky_status[index]} \n\n {dt.strftime("%Y-%m-%d %H:%M")}"
                captions.append(dt)
            st.image(images, width=100, caption=captions)
                    
    except KeyError:
        st.error("This city doesn't exist")
                