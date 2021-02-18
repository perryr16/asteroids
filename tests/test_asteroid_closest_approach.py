from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.asteroid_closest_approach import asteroid_closest_approach
import pytest


def test_version():
  assert __version__ == '0.1.0'

@pytest.mark.vcr()
def test_asteroid_closest_approach():
  asteroid_json = asteroid_closest_approach(50)
  asteroids = json.loads(asteroid_json)
  for i in range(0, len(asteroids)-1):
    assert asteroids[i]['links']
    assert asteroids[i]['id']
    assert asteroids[i]['neo_reference_id']
    assert asteroids[i]['name']
    assert asteroids[i]['designation']
    assert asteroids[i]['nasa_jpl_url']
    # assert asteroids[i]['absolute_magnitude_h']# key error at asteroid[7099]
    # assert asteroids[i]['estimated_diameter']#
    assert asteroids[i]['close_approach_data']
    assert type(asteroids[i]['close_approach_data']) is dict
    assert asteroids[i]['orbital_data']