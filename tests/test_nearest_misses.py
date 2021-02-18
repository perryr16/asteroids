from asteroids import __version__
import unittest, requests, json, os, pytest
from dotenv import load_dotenv
load_dotenv()
from asteroids.nearest_misses import nearest_misses

def test_version():
  assert __version__ == '0.1.0'

@pytest.mark.vcr()
def test_nearest_misses():
  #limiting to 5 pages as I know asteroid_closest_approach is functional
  asteroids_json = nearest_misses(50)
  asteroids = json.loads(asteroids_json)
  d0 = asteroids[0]['close_approach_data']['miss_distance']['miles']
  d1 = asteroids[1]['close_approach_data']['miss_distance']['miles']
  d2 = asteroids[2]['close_approach_data']['miss_distance']['miles']
  d3 = asteroids[3]['close_approach_data']['miss_distance']['miles']
  d4 = asteroids[4]['close_approach_data']['miss_distance']['miles']
  d5 = asteroids[5]['close_approach_data']['miss_distance']['miles']
  d5 = asteroids[5]['close_approach_data']['miss_distance']['miles']
  d6 = asteroids[6]['close_approach_data']['miss_distance']['miles']
  d7 = asteroids[7]['close_approach_data']['miss_distance']['miles']
  d8 = asteroids[8]['close_approach_data']['miss_distance']['miles']
  d9 = asteroids[9]['close_approach_data']['miss_distance']['miles']

  assert len(asteroids) == 10
  assert d0 < d1
  assert d1 < d2
  assert d2 < d3
  assert d3 < d4
  assert d4 < d5
  assert d5 < d6
  assert d6 < d7
  assert d7 < d8
  assert d8 < d9

  for i in range (0, 10):
    assert asteroids[i]['links']
    assert asteroids[i]['id']
    assert asteroids[i]['neo_reference_id']
    assert asteroids[i]['name']
    assert asteroids[i]['designation']
    assert asteroids[i]['nasa_jpl_url']
    assert asteroids[i]['close_approach_data']
    assert type(asteroids[i]['close_approach_data']) is dict
    assert asteroids[i]['orbital_data']
  