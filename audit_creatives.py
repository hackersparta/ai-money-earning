"""Audit all 4 ads for Saturday references and wrong dates"""
import urllib.request, json

TOKEN = 'EAAUVhY8Tf9YBQ1Kzh9vmq1OdLCogdMwHlOZBGfCCV6NHrZAaqEOnE8gNI1KMeHvh4fgfxVTZAZC1YnPPW9IVoGAklVrx5RjkLwrPBU2csx5oPesXRlfRAsEuKeGS19YrHXLSaCJh4wCmmBQoNNxN1ZCZAXrcE5UdUICWE8euCWILZBn5gDIy45ZBAaVx7NgJRuLZC'

# All ad creatives
creatives = {
    'Housewives-Independence': '948088544568360',
    'Housewives-Value': '956929220090605',
    'Students-Speed': None,  # need to find
    'Students-Fear': None,   # need to find
}

# First get ad details to find creative IDs
print('Getting all ads...')
for adset_name, adset_id in [('Housewives', '6951801137468'), ('Students', '6951039860868')]:
    url = 'https://graph.facebook.com/v19.0/' + adset_id + '/ads?fields=id,name,creative&access_token=' + TOKEN
    r = json.loads(urllib.request.urlopen(url).read())
    for ad in r.get('data', []):
        print(ad['name'], '-> creative:', ad.get('creative', {}).get('id'))

print()

# Get all creative IDs
all_creatives = ['948088544568360', '956929220090605']

# Get Students creatives
for adset_id in ['6951039860868']:
    url = 'https://graph.facebook.com/v19.0/' + adset_id + '/ads?fields=name,creative&access_token=' + TOKEN
    r = json.loads(urllib.request.urlopen(url).read())
    for ad in r.get('data', []):
        cid = ad.get('creative', {}).get('id')
        if cid and cid not in all_creatives:
            all_creatives.append(cid)

# Now fetch each creative body/title/description
print('=' * 70)
for cid in all_creatives:
    url = 'https://graph.facebook.com/v19.0/' + cid + '?fields=name,title,body,object_story_spec&access_token=' + TOKEN
    r = json.loads(urllib.request.urlopen(url).read())
    
    name = r.get('name', 'Unknown')
    body = r.get('body', '')
    title = r.get('title', '')
    oss = r.get('object_story_spec', {})
    ld = oss.get('link_data', {})
    desc = ld.get('description', '')
    link = ld.get('link', '')
    msg = ld.get('message', '')
    
    print(f'\nCREATIVE: {name} (ID: {cid})')
    print(f'Title: {title}')
    print(f'Description: {desc}')
    print(f'Link: {link}')
    print(f'Body (primary text):')
    print(body)
    
    # Check for Saturday references
    has_saturday = 'saturday' in body.lower() or 'saturday' in title.lower() or 'saturday' in desc.lower()
    has_saturday_tamil = 'Saturday' in body or 'சனிக்கிழமை' in body
    print(f'\n  >> Contains "Saturday": {has_saturday or has_saturday_tamil}')
    print('=' * 70)
