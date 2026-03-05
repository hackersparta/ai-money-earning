import urllib.request, json

token = 'EAAUVhY8Tf9YBQ9vVDYns8c2ZC8cAIvXrFUVapkvYdlHXTZBcTtwPsPMfVcGpoi5pv852lo7H0ZCC88JUiHaIBEZAZAyv30MDjx19qkF0hb35MnRbCIPECz7ZANpylkr4ZBmMtPZCiW2xFiDTFtjXBxEq4sJCDt9LEleCYZCDldKag6IsoUyINFj8ZBIqNeNoZAjC4SWASI2TQQRPCc1HAF7a2U1WQ4aCNY9HIofEJ9o5rRAHk0pHHuCQXXaICEWTZCMj87ijRS78omwEba7Tf4aZCrZBr9'

# Get ad accounts
url = f'https://graph.facebook.com/v19.0/me/adaccounts?fields=id,name,account_status,currency&access_token={token}'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
data = json.loads(resp.read())
print('=== AD ACCOUNTS ===')
for acc in data.get('data', []):
    print(f"  {acc['id']} | {acc['name']} | status={acc['account_status']} | {acc['currency']}")

# Get pages
url2 = f'https://graph.facebook.com/v19.0/me/accounts?fields=id,name&access_token={token}'
req2 = urllib.request.Request(url2)
resp2 = urllib.request.urlopen(req2)
data2 = json.loads(resp2.read())
print('=== PAGES ===')
for page in data2.get('data', []):
    print(f"  {page['id']} | {page['name']}")
