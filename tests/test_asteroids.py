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
    asteroids = asteroid_closest_approach()
    assert asteroids[0]['links']
    assert asteroids[0]['id']
    assert asteroids[0]['neo_reference_id']
    assert asteroids[0]['name']
    assert asteroids[0]['name_limited']
    assert asteroids[0]['designation']
    assert asteroids[0]['nasa_jpl_url']
    assert asteroids[0]['absolute_magnitude_h']
    assert asteroids[0]['estimated_diameter']
    assert asteroids[0]['is_potentially_hazardous_asteroid'] == False
    assert asteroids[0]['close_approach_data']
    assert asteroids[0]['close_approach_data']
    assert asteroids[0]['orbital_data']
    assert asteroids[0]['is_sentry_object'] == False