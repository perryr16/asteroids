import requests 
import os
import json

def browse_neos(page_num = 0):
    key = os.getenv('NASA_KEY')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page={page_num}'
    return requests.get(url).json()
    

