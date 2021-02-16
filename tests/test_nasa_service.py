from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.services import browse_neos

def test_version():
    assert __version__ == '0.1.0'
    
def test_nasa():
    key = os.getenv('NASA_KEY')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page=1'
    res = requests.get(url).json()
    keys = list(res)
    assert keys == ['links', 'page', 'near_earth_objects']

def test_browse_neos():
  res = browse_neos()
  keys = list(res)
  assert keys == ['links', 'page', 'near_earth_objects']
