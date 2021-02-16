from asteroids import __version__
import unittest
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from asteroids.month_closest_approaches import month_closest_approaches

def test_version():
    assert __version__ == '0.1.0'

def test_month_closest_approaches():
  res_json = month_closest_approaches('2020-01') 
  res = json.loads(res_json)
  assert list(res) == ['month', 'element_count', 'near_earth_objects']
  assert res['month'] == '2020-01'
  assert res['element_count'] == 290 
  assert list(res['near_earth_objects']) == ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04']
  assert len(res['near_earth_objects']['2020-01-01']) == 14
  assert len(res['near_earth_objects']['2020-01-02']) == 19
  

