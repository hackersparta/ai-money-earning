"""Activate both ad sets for today March 7, 2026 until 11:59 PM IST"""
import urllib.request, urllib.parse, json

TOKEN = 'EAAUVhY8Tf9YBQ1Kzh9vmq1OdLCogdMwHlOZBGfCCV6NHrZAaqEOnE8gNI1KMeHvh4fgfxVTZAZC1YnPPW9IVoGAklVrx5RjkLwrPBU2csx5oPesXRlfRAsEuKeGS19YrHXLSaCJh4wCmmBQoNNxN1ZCZAXrcE5UdUICWE8euCWILZBn5gDIy45ZBAaVx7NgJRuLZC'
CAMPAIGN_ID = '6951039185468'

def api_post(endpoint, params):
    params['access_token'] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request('https://graph.facebook.com/v19.0/' + endpoint, data=data, method='POST')
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except Exception as e:
        err = e.read().decode()
        print('  ERROR:', err)
        return None

# End time: March 7, 2026 11:59 PM IST
end_time = '2026-03-07T23:59:00+0530'

# Step 1: Activate Campaign
print('1. Activating Campaign...')
r = api_post(CAMPAIGN_ID, {'status': 'ACTIVE'})
print('  Campaign:', r)

# Step 2: Activate Housewives Ad Set with end time
print('2. Activating Housewives Ad Set...')
r = api_post('6951801137468', {'status': 'ACTIVE', 'end_time': end_time})
print('  Housewives AdSet:', r)

# Step 3: Activate Students Ad Set with end time
print('3. Activating Students Ad Set...')
r = api_post('6951039860868', {'status': 'ACTIVE', 'end_time': end_time})
print('  Students AdSet:', r)

# Step 4: Activate all ads
print('4. Activating all ads...')
for adset_name, adset_id in [('Housewives', '6951801137468'), ('Students', '6951039860868')]:
    url = 'https://graph.facebook.com/v19.0/' + adset_id + '/ads?fields=id,name,status&access_token=' + TOKEN
    ads = json.loads(urllib.request.urlopen(url).read())
    for ad in ads.get('data', []):
        r = api_post(ad['id'], {'status': 'ACTIVE'})
        ad_name = ad.get('name', ad['id'])
        print('  ' + adset_name + ' - ' + ad_name + ': ' + str(r))

print()
print('ALL DONE! Both ad sets ACTIVE until 11:59 PM IST tonight (March 7).')
