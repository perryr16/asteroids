import requests 
import os
import json

def asteroid_closest_approach():
    asteroids = []
    nasa_data = browse_neos()
    asteroids = find_closest_approach_and_append(nasa_data, asteroids)
    
    # for asteroid in asteroids['near_earth_objects']:
    #   asteroids['close_approach_data'] = min(asteroid['close_approach_data'], key=lambda x: x['miss_distance']['astronomical'])
    return asteroids

def find_closest_approach_and_append(nasa_data, asteroids):
  for asteroid in nasa_data['near_earth_objects']:
    asteroid['close_approach_data'] = min(asteroid['close_approach_data'], key=lambda close_approach: close_approach['miss_distance']['astronomical'])
    asteroids.append(asteroid)
  return asteroids

def browse_neos(page_num = 0):
    key = os.getenv('NASA_KEY')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page={page_num}'
    return requests.get(url).json()
    

