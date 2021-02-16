import requests 
import os
import json

def asteroid_closest_approach():
    key = os.getenv('NASA_KEY')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page=1'
    res = requests.get(url).json()
    raw_keys = list(res)
    breakpoint()
    
