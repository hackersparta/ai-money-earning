"""Schedule ads to activate at 8 AM IST and deactivate at 11:59 PM IST on March 7, 2026"""
import urllib.request, urllib.parse, json, time, datetime

TOKEN = 'EAAUVhY8Tf9YBQ1Kzh9vmq1OdLCogdMwHlOZBGfCCV6NHrZAaqEOnE8gNI1KMeHvh4fgfxVTZAZC1YnPPW9IVoGAklVrx5RjkLwrPBU2csx5oPesXRlfRAsEuKeGS19YrHXLSaCJh4wCmmBQoNNxN1ZCZAXrcE5UdUICWE8euCWILZBn5gDIy45ZBAaVx7NgJRuLZC'

CAMPAIGN_ID = '6951039185468'
ADSET_IDS = ['6951801137468', '6951039860868']
AD_IDS = ['6951801143868', '6951801152468', '6951039903268', '6951039894868']

IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

def api_post(endpoint, params):
    params['access_token'] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request('https://graph.facebook.com/v19.0/' + endpoint, data=data, method='POST')
    try:
        return json.loads(urllib.request.urlopen(req).read())
    except Exception as e:
        print('  ERROR:', e.read().decode())
        return None

def activate_all():
    print('ACTIVATING campaign...')
    print(api_post(CAMPAIGN_ID, {'status': 'ACTIVE'}))
    for adset_id in ADSET_IDS:
        print(f'ACTIVATING ad set {adset_id}...')
        print(api_post(adset_id, {'status': 'ACTIVE', 'end_time': '2026-03-07T23:59:00+0530'}))
    for ad_id in AD_IDS:
        print(f'ACTIVATING ad {ad_id}...')
        print(api_post(ad_id, {'status': 'ACTIVE'}))

def now_ist():
    return datetime.datetime.now(IST)

# Target: 8:00 AM IST on March 7, 2026
target = datetime.datetime(2026, 3, 7, 8, 0, 0, tzinfo=IST)

current = now_ist()
print(f'Current IST: {current.strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Target time: {target.strftime("%Y-%m-%d %H:%M:%S")} IST')

if current >= target:
    print('It is already past 8 AM IST. Activating now!')
    activate_all()
else:
    wait_seconds = (target - current).total_seconds()
    print(f'Waiting {wait_seconds:.0f} seconds ({wait_seconds/3600:.1f} hours) until 8 AM IST...')
    print('DO NOT close this terminal window!')
    print()
    
    while now_ist() < target:
        remaining = (target - now_ist()).total_seconds()
        mins = int(remaining // 60)
        print(f'\r  Waiting... {mins} minutes remaining   ', end='', flush=True)
        time.sleep(30)
    
    print('\n')
    print('=' * 50)
    print('8 AM IST REACHED! Activating ads now...')
    print('=' * 50)
    activate_all()

print()
print('DONE! Ads will run until 11:59 PM IST tonight.')
