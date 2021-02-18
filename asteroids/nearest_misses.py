import json
from .asteroid_closest_approach import asteroid_closest_approach

def nearest_misses(page_limit = None):
  asteroids = json.loads(asteroid_closest_approach(page_limit))
  asteroids_by_distance = sorted(asteroids, key=lambda data: data['close_approach_data']['miss_distance']['miles'])
  top_10 = asteroids_by_distance[0:10]
  # mapped_obj = map(lambda ast: ast['close_approach_data']['miss_distance']['miles'], top_10)
  # mapped = list(mapped_obj)
  return json.dumps(top_10)