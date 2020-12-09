from datetime import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv
import urllib.request
import json
import sys
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

JSON_URL = os.getenv('JSON_URL')
SESSION = os.getenv('SESSION')
if len(sys.argv) <= 1:
   sys.exit('No day provided as argument')
DAY = str(sys.argv[1])

req = urllib.request.Request(JSON_URL, None, { 'Cookie': 'session=' + SESSION }, method='GET')

def getUserCompletionDay(ms, mid, DAY):
   stars = ms[mid]['completion_day_level']
   firstDayTimestamp = int(stars[DAY]['1']['get_star_ts'])
   secondDayTimestamp = int(stars[DAY]['2']['get_star_ts']) if '2' in stars[DAY].keys() else 0

   return [ms[mid]['name']] + [firstDayTimestamp] + [secondDayTimestamp]

with urllib.request.urlopen(req) as response:
   json_response = response.read()
   json = json.loads(json_response)

   ms = json['members']
   completed = [getUserCompletionDay(ms, mid, DAY) for mid in ms if DAY in ms[mid]['completion_day_level'].keys()]

   completedSortedStarOne = sorted(completed, key=lambda tup: tup[1])
   completedSortedStarTwo = filter(lambda x: x[2] > 0, sorted(completed, key=lambda tup: tup[2]))

   print(f'=== DAY {DAY} ===')
   print('--- STAR 1 ---')
   [print(datetime.fromtimestamp(x[1]), x[0]) for x in completedSortedStarOne]
   print('\n')
   print('--- STAR 2 ---')
   [print(datetime.fromtimestamp(x[2]), x[0]) for x in completedSortedStarTwo]