from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.asteroids import asteroid_closest_approach

def test_version():
    assert __version__ == '0.1.0'

# def test_nasa():
#     key = os.getenv('NASA_KEY')
#     url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page=1'
#     res = requests.get(url).json()
#     raw_keys = list(res)
#     assert raw_keys == ['links', 'page', 'near_earth_objects']

def test_asteroid_closest_approach():
    asteroid_closest_approach()
    # keys = list(asteroids)
    # assert keys = ['asteroids']