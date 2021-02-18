from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.services import browse_neos, feed_neos
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.vcr()
def test_nasa():
    key = os.getenv('NASA_KEY')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page=1'
    res = requests.get(url).json()
    keys = list(res)
    assert keys == ['links', 'page', 'near_earth_objects']

@pytest.mark.vcr()
def test_browse_neos():
  res = browse_neos()
  keys = list(res)
  assert keys == ['links', 'page', 'near_earth_objects']

@pytest.mark.vcr()
def test_feed_neos():
  start_date = '2020-01-01'
  end_date = '2020-01-08'
  res = feed_neos(start_date, end_date)
  keys = list(res)
  assert keys == ['links', 'element_count', 'near_earth_objects']
