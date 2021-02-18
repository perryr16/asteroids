import datetime, calendar, math, json
from .services import feed_neos

def month_closest_approaches(start_date):
  num_days = num_days_in_month(start_date)
  num_intervals = math.ceil(num_days/7)
  intervals = format_intervals(start_date, num_days, num_intervals)
  results = loop_through_intervals(start_date, intervals)
  return json.dumps(results)

def loop_through_intervals(start_date, intervals):
  results = {'month': start_date, 'element_count':0, 'near_earth_objects':{}}
  for interval in intervals:
    nasa_data = feed_neos(interval[0], interval[1])
    results['element_count'] += nasa_data['element_count']
    for k,v in nasa_data['near_earth_objects'].items():
      results['near_earth_objects'][k] = v
  return results 

def format_intervals(start_date, num_days, num_intervals):
  intervals = []
  for x in range(0, num_intervals):
    start = x * 7 + 1 
    end = start + 6 
    if end > num_days: end = num_days
    start_interval = f'{start_date}-{str(start).zfill(2)}'
    end_interval = f'{start_date}-{str(end).zfill(2)}'
    intervals.append([start_interval, end_interval])
  return intervals

def num_days_in_month(start_date):
  date_list = start_date.split('-')
  year = int(date_list[0])
  month = int(date_list[1])
  return calendar.monthrange(year, month)[1]
