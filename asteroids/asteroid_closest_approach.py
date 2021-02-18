import json, math
from .services import browse_neos


def asteroid_closest_approach(page_limit = None):
  asteroids, nasa_data = [], browse_neos()
  nasa_pages = nasa_data['page']['total_pages']
  total_pages = page_limit if page_limit and nasa_pages > page_limit else nasa_pages
  results = loop_through_pages(total_pages, nasa_data, asteroids)
  return json.dumps(results) 


def loop_through_pages(total_pages, nasa_data, asteroids):
  for page in range(0, total_pages):
    # print (page)
    nasa_data = browse_neos(page)
    asteroids = find_closest_approach_and_append(nasa_data, asteroids)
  return asteroids

def find_closest_approach_and_append(nasa_data, asteroids):
  for asteroid in nasa_data['near_earth_objects']:
    if asteroid['close_approach_data']:
      asteroid['close_approach_data'] = min(asteroid['close_approach_data'], key=lambda data: data['miss_distance']['miles'])
      asteroids.append(asteroid)
  return asteroids

# (Pdb) pp asteroids[0]['close_approach_data']
# {'close_approach_date': '2137-01-25',
#  'close_approach_date_full': '2137-Jan-25 14:12',
#  'epoch_date_close_approach': 5272179120000,
#  'miss_distance': {'astronomical': '0.1494623118',
#                    'kilometers': '22359243.490555866',
#                    'lunar': '58.1408392902',
#                    'miles': '13893389.6599923108'},
#  'orbiting_body': 'Earth',
#  'relative_velocity': {'kilometers_per_hour': '20931.393257436',
#                        'kilometers_per_second': '5.8142759048',
#                        'miles_per_hour': '13005.953771544'}}
