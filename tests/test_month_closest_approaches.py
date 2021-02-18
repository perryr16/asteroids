from asteroids import __version__
import unittest, requests, json, os, pytest
from dotenv import load_dotenv
load_dotenv()
from asteroids.month_closest_approaches import month_closest_approaches

def test_version():
  assert __version__ == '0.1.0'

@pytest.mark.vcr()
def test_month_closest_approaches():
  res_json = month_closest_approaches('2020-01') 
  res = json.loads(res_json)
  assert list(res) == ['month', 'element_count', 'near_earth_objects']
  assert res['month'] == '2020-01'
  assert res['element_count'] == 528 
  
  dates = ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', 
            '2020-01-06', '2020-01-07', '2020-01-10', '2020-01-11', '2020-01-12', 
            '2020-01-13', '2020-01-14', '2020-01-08', '2020-01-09', '2020-01-20', 
            '2020-01-21', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', 
            '2020-01-19', '2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', 
            '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-30', '2020-01-31', 
            '2020-01-29']

  assert list(res['near_earth_objects']) == dates
  assert len(res['near_earth_objects']['2020-01-01']) == 14
  assert len(res['near_earth_objects']['2020-01-02']) == 19
  

