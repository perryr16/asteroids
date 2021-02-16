import datetime, calendar, math
from .services import feed_neos

def month_closest_approaches(start_date):
  asteroids = {'month': start_date, 'element_count':0, 'near_earth_objects':{}}
  num_days = num_days_in_month(start_date)
  num_intervals = math.ceil(num_days/7)
  intervals = format_intervals(start_date, num_days, num_intervals)
  for interval in intervals:
    # nasa_data = feed_neos(interval[0], interval[1])
    nasa_data = feed_neos('2020-01-01', '2020-01-04')
    asteroids['element_count'] += nasa_data['element_count']
    for k,v in nasa_data['near_earth_objects'].items():
      asteroids['near_earth_objects'][k] = v
  
  breakpoint()

def num_days_in_month(start_date):
  date_list = start_date.split('-')
  year = int(date_list[0])
  month = int(date_list[1])
  return calendar.monthrange(year, month)[1]

def format_intervals(start_date, num_days, num_intervals):
  intervals = []
  for x in range(0, num_intervals):
    start = x*7+1 # 1, 8, 15, 22, 29
    end = start + 6 # 7, 14, 21, 28, 3
    if end > num_days: end = num_days
    start_interval = f'{start_date}-{str(start).zfill(2)}'
    end_interval = f'{start_date}-{str(end).zfill(2)}'
    intervals.append([start_interval, end_interval])
  return intervals