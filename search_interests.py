import urllib.request, json, urllib.parse

TOKEN = 'EAAUVhY8Tf9YBQ9vVDYns8c2ZC8cAIvXrFUVapkvYdlHXTZBcTtwPsPMfVcGpoi5pv852lo7H0ZCC88JUiHaIBEZAZAyv30MDjx19qkF0hb35MnRbCIPECz7ZANpylkr4ZBmMtPZCiW2xFiDTFtjXBxEq4sJCDt9LEleCYZCDldKag6IsoUyINFj8ZBIqNeNoZAjC4SWASI2TQQRPCc1HAF7a2U1WQ4aCNY9HIofEJ9o5rRAHk0pHHuCQXXaICEWTZCMj87ijRS78omwEba7Tf4aZCrZBr9'

queries = ['work from home', 'online shopping', 'cooking', 'parenting', 
           'higher education', 'technology', 'career', 'freelancing',
           'artificial intelligence', 'digital marketing']

for q in queries:
    url = f'https://graph.facebook.com/v19.0/search?type=adinterest&q={urllib.parse.quote(q)}&access_token={TOKEN}'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    results = data.get('data', [])[:3]
    print(f'\n--- {q} ---')
    for r in results:
        print(f"  ID: {r['id']} | Name: {r['name']} | Size: {r.get('audience_size_lower_bound', '?')}-{r.get('audience_size_upper_bound', '?')}")
