1. 'https://api.propublica.org/congress/v1/house/votes/recent.json'

2. 'https://api.propublica.org/congress/v1/members/both/mo/current.json' and 'https://api.propublica.org/congress/v1/members/house/mo/current.json'

3. Senate:  https://api.propublica.org/congress v1/senate/80-115/sessions/1/votes/111.json

4.
import json 
import requests

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'

url = 'https://api.propublica.org/congress/v1/115/house/members/leaving.json'

response = requests.get(url, headers={"X-API-Key": API_KEY}).content

data = json.loads(response)

print data['results'][0]['members'][0]['first_name'], data['results'][0]['members'][0]['last_name']