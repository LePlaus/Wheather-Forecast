from json import load
from urllib import request
from dotenv import load_dotenv
import os
from numpy import require
import requests
from datetime import datetime



def get_data(place, forecast_days=None, kind=None):
    
    load_dotenv()
    api_key = os.getenv("WAEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}"

    response = requests.get(url)
    content = response.json()
    listed = content["list"]
    
    dates = [datetime.utcfromtimestamp(i["dt"]) for i in listed]
    main_data = [i["main"] for i in listed]
    tempuratures = [i["temp"] for i in main_data]
    print(main_data)

    return dates, tempuratures



if __name__ == "__main__":
    get_data(place="Tokyo",forecast_days=3,kind="Tempurature")