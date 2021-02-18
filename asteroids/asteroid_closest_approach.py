import json
from .services import browse_neos


def asteroid_closest_approach():
  asteroids, nasa_data = [], browse_neos()
  total_pages = nasa_data['page']['total_pages']
  # total_pages = 4 # to prevent lengthy iteration during testing
  results = loop_through_pages(total_pages, nasa_data, asteroids)
  return json.dumps(results) 

def loop_through_pages(total_pages, nasa_data, asteroids):
  for page in range(0, total_pages):
    nasa_data = browse_neos(page)
    asteroids = find_closest_approach_and_append(nasa_data, asteroids)
  return asteroids

def find_closest_approach_and_append(nasa_data, asteroids):
  for asteroid in nasa_data['near_earth_objects']:
    asteroid['close_approach_data'] = min(asteroid['close_approach_data'], key=lambda data: data['miss_distance']['miles'])
    asteroids.append(asteroid)
  return asteroids
