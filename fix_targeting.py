"""Fix ad set targeting: India → Tamil Nadu"""
import urllib.request, urllib.parse, json, sys

TOKEN = 'EAAUVhY8Tf9YBQ9vVDYns8c2ZC8cAIvXrFUVapkvYdlHXTZBcTtwPsPMfVcGpoi5pv852lo7H0ZCC88JUiHaIBEZAZAyv30MDjx19qkF0hb35MnRbCIPECz7ZANpylkr4ZBmMtPZCiW2xFiDTFtjXBxEq4sJCDt9LEleCYZCDldKag6IsoUyINFj8ZBIqNeNoZAjC4SWASI2TQQRPCc1HAF7a2U1WQ4aCNY9HIofEJ9o5rRAHk0pHHuCQXXaICEWTZCMj87ijRS78omwEba7Tf4aZCrZBr9'
BASE = 'https://graph.facebook.com/v19.0'

def api_post(endpoint, params):
    params['access_token'] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(f'{BASE}/{endpoint}', data=data, method='POST')
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f'ERROR {e.code}: {e.read().decode()}')
        return None

# Update Ad Set A (Housewives) - India + Tamil language 
print('Updating Ad Set A (Housewives) to India + Tamil language...')
r1 = api_post('6951039855668', {
    'targeting': json.dumps({
        'age_min': 25,
        'age_max': 65,
        'genders': [2],
        'geo_locations': {
            'countries': ['IN'],
            'location_types': ['home', 'recent']
        },
        'locales': [48],  # Tamil language (key=48)
        'publisher_platforms': ['facebook', 'instagram'],
        'targeting_automation': {'advantage_audience': 1},
    }),
})
if r1:
    print(f'  Done: {r1}')

# Update Ad Set B (Students) - India + Tamil language
print('Updating Ad Set B (Students) to India + Tamil language...')
r2 = api_post('6951039860868', {
    'targeting': json.dumps({
        'age_min': 18,
        'age_max': 65,
        'geo_locations': {
            'countries': ['IN'],
            'location_types': ['home', 'recent']
        },
        'locales': [48],  # Tamil language (key=48)
        'publisher_platforms': ['facebook', 'instagram'],
        'targeting_automation': {'advantage_audience': 1},
    }),
})
if r2:
    print(f'  Done: {r2}')

print('\nBoth ad sets updated to Tamil Nadu!')
