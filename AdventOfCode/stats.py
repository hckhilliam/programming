import requests
import json

resp = requests.get(
    'https://adventofcode.com/2021/leaderboard/private/view/1564727.json',
    headers={
        'Cookie': 'session=53616c7465645f5f392cfb29cbc6423d1e862fab5184d51b5495cc383ce84032e040210adab76aa85dcca2406511cdcd'
    }
)

data = json.loads(resp.content)
members = data['members']

deltas = {}
for member in members.values():
    delta = {}
    days = member['completion_day_level']
    for day, results in days.items():
        if len(results.keys()) > 1:
            delta[day] = results['2']['get_star_ts'] - results['1']['get_star_ts']
    deltas[member['name']] = delta

for name, ds in deltas.items():
    print(name)
    i = 1
    for i in range(25):
        if str(i) in ds:
            print(f'Day {i}: {ds[str(i)]}')
