from json import load
import math
from urllib import request
from dotenv import load_dotenv
import os
from numpy import require
import requests
from datetime import datetime



def get_data(place, fc_days, kind):
    
    load_dotenv()
    api_key = os.getenv("WAEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    match kind:
        case "Tempurature":
            listed = content["list"]
            main_data = [i["main"] for i in listed]
            tempuratures = [i["temp"] for i in main_data][0:int(fc_days)*5]
            dates = [datetime.utcfromtimestamp(i["dt"]) for i in listed][0:int(fc_days)*5]
            
            return dates, tempuratures
        
        case "Sky":
            pass


if __name__ == "__main__":
    get_data(place="Tokyo",fc_days=3,kind="Tempurature")