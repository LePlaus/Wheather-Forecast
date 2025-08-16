from json import load
from dotenv import load_dotenv
import os
import requests
from datetime import datetime


def get_data(place, fc_days, kind):
    
    load_dotenv()
    api_key = os.getenv("WAEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    
    listed = content["list"][0:int(fc_days)*8]
    dates = [datetime.fromtimestamp(i["dt"]) for i in listed]
    

    if kind == "Tempurature":
        
        main_data = [i["main"] for i in listed]
        tempuratures = [i["temp"] for i in main_data]
        
        return dates, tempuratures
    
    if kind == "Sky":
        
        weather = [i["weather"] for i in listed]
        sky_status = [i[0]["main"] for i in weather]
        sky_description = [i[0]["description"] for i in weather]
        return dates, sky_status, sky_description


if __name__ == "__main__":
    get_data(place="Tokyo",fc_days=3,kind="Sky")