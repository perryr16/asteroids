from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.asteroid_closest_approach import asteroid_closest_approach

def test_version():
    assert __version__ == '0.1.0'

def test_asteroid_closest_approach():
    asteroid_json = asteroid_closest_approach()
    asteroids = json.loads(asteroid_json)
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

    assert asteroids[-1]['links']
    assert asteroids[-1]['id']
    assert asteroids[-1]['neo_reference_id']
    assert asteroids[-1]['name']
    # assert asteroids[-1]['name_limited']
    assert asteroids[-1]['designation']
    assert asteroids[-1]['nasa_jpl_url']
    assert asteroids[-1]['absolute_magnitude_h']
    assert asteroids[-1]['estimated_diameter']
    # assert asteroids[-1]['is_potentially_hazardous_asteroid'] == False
    assert asteroids[-1]['close_approach_data']
    assert asteroids[-1]['close_approach_data'] 
    assert asteroids[-1]['orbital_data']
    assert asteroids[-1]['is_sentry_object'] == False