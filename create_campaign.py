"""
Meta Ads Campaign Creator
Creates: 1 Campaign → 2 Ad Sets → 2 Ads each = 4 Ads total
Budget: Rs.200/day (Rs.100 per ad set)
"""
import urllib.request, urllib.parse, json, os, sys, time

TOKEN = 'EAAUVhY8Tf9YBQ9vVDYns8c2ZC8cAIvXrFUVapkvYdlHXTZBcTtwPsPMfVcGpoi5pv852lo7H0ZCC88JUiHaIBEZAZAyv30MDjx19qkF0hb35MnRbCIPECz7ZANpylkr4ZBmMtPZCiW2xFiDTFtjXBxEq4sJCDt9LEleCYZCDldKag6IsoUyINFj8ZBIqNeNoZAjC4SWASI2TQQRPCc1HAF7a2U1WQ4aCNY9HIofEJ9o5rRAHk0pHHuCQXXaICEWTZCMj87ijRS78omwEba7Tf4aZCrZBr9'
AD_ACCOUNT = 'act_494034697374591'
PAGE_ID = '1455821964711020'
API_VERSION = 'v19.0'
BASE_URL = f'https://graph.facebook.com/{API_VERSION}'

IMAGES_DIR = r'C:\Users\w136733\OneDrive - Worldline SA\Projects\Openclaw Vscode\Creatives\Tamil'

def api_post(endpoint, params):
    params['access_token'] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f'{BASE_URL}/{endpoint}'
    req = urllib.request.Request(url, data=data, method='POST')
    try:
        resp = urllib.request.urlopen(req)
        result = json.loads(resp.read())
        return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f'ERROR {e.code}: {error_body}')
        sys.exit(1)

def upload_image(image_path):
    """Upload image to ad account and return image hash"""
    import base64
    with open(image_path, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode()
    
    result = api_post(f'{AD_ACCOUNT}/adimages', {
        'bytes': img_data,
    })
    # Response: {"images": {"bytes": {"hash": "xxx", ...}}}
    images = result.get('images', {})
    for key in images:
        return images[key]['hash']
    return None

# ============================================================
# STEP 1: Upload all 4 images
# ============================================================
print('=' * 50)
print('UPLOADING IMAGES...')
print('=' * 50)

image_hashes = {}
for i in range(1, 5):
    path = os.path.join(IMAGES_DIR, f'Image {i}.png')
    if not os.path.exists(path):
        print(f'  ERROR: {path} not found!')
        sys.exit(1)
    print(f'  Uploading Image {i}.png...', end=' ')
    h = upload_image(path)
    image_hashes[i] = h
    print(f'hash={h}')

# ============================================================
# STEP 2: Create Campaign (PAUSED — you activate when ready)
# ============================================================
print('\n' + '=' * 50)
print('CREATING CAMPAIGN...')
print('=' * 50)

# Use existing campaign if it was already created
existing_campaign_id = '6951039185468'
if existing_campaign_id:
    campaign_id = existing_campaign_id
    print(f'  Using existing Campaign ID: {campaign_id}')
else:
    campaign = api_post(f'{AD_ACCOUNT}/campaigns', {
        'name': 'AI-Workshop-Tamil-Traffic-20260305',
        'objective': 'OUTCOME_TRAFFIC',
        'status': 'PAUSED',
        'special_ad_categories': '[]',
        'is_adset_budget_sharing_enabled': 'false',
    })
    campaign_id = campaign['id']
    print(f'  Campaign ID: {campaign_id}')

# ============================================================
# STEP 3: Create Ad Sets
# ============================================================
print('\n' + '=' * 50)
print('CREATING AD SETS...')
print('=' * 50)

# Ad Set A: Housewives (25-45, Female, Tamil Nadu)
adset_a = api_post(f'{AD_ACCOUNT}/adsets', {
    'name': 'Housewives-25-45-TN',
    'campaign_id': campaign_id,
    'daily_budget': '10000',  # Rs.100 in paise
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'LINK_CLICKS',
    'bid_strategy': 'LOWEST_COST_WITHOUT_CAP',
    'status': 'PAUSED',
    'targeting': json.dumps({
        'age_min': 25,
        'age_max': 45,
        'genders': [2],  # Female
        'geo_locations': {
            'countries': ['IN'],
            'location_types': ['home', 'recent']
        },
        'flexible_spec': [{
            'interests': [
                {'id': '6003346592981', 'name': 'Online shopping'},
                {'id': '6003343813828', 'name': 'Telecommuting'},
                {'id': '6003659420716', 'name': 'Cooking'},
                {'id': '6003232518610', 'name': 'Parenting'},
            ]
        }],
        'publisher_platforms': ['facebook', 'instagram'],
        'targeting_automation': {'advantage_audience': 0},
    }),
    'promoted_object': json.dumps({
        'page_id': PAGE_ID,
    }),
})
adset_a_id = adset_a['id']
print(f'  Ad Set A (Housewives): {adset_a_id}')

# Ad Set B: Students (18-25, All, Tamil Nadu)
adset_b = api_post(f'{AD_ACCOUNT}/adsets', {
    'name': 'Students-18-25-TN',
    'campaign_id': campaign_id,
    'daily_budget': '10000',  # Rs.100 in paise
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'LINK_CLICKS',
    'bid_strategy': 'LOWEST_COST_WITHOUT_CAP',
    'status': 'PAUSED',
    'targeting': json.dumps({
        'age_min': 18,
        'age_max': 30,
        'geo_locations': {
            'countries': ['IN'],
            'location_types': ['home', 'recent']
        },
        'flexible_spec': [{
            'interests': [
                {'id': '6003270811593', 'name': 'Higher education'},
                {'id': '6003985771306', 'name': 'Technology'},
                {'id': '6003165927235', 'name': 'Career'},
                {'id': '6002898176962', 'name': 'Artificial intelligence'},
            ]
        }],
        'publisher_platforms': ['facebook', 'instagram'],
        'targeting_automation': {'advantage_audience': 0},
    }),
    'promoted_object': json.dumps({
        'page_id': PAGE_ID,
    }),
})
adset_b_id = adset_b['id']
print(f'  Ad Set B (Students): {adset_b_id}')

# ============================================================
# STEP 4: Create Ad Creatives + Ads
# ============================================================
print('\n' + '=' * 50)
print('CREATING ADS...')
print('=' * 50)

ads_config = [
    # Ad Set A ads
    {
        'adset_id': adset_a_id,
        'name': 'Housewives-Independence',
        'image_hash': image_hashes[1],
        'message': (
            '\u0bb5\u0bc0\u0b9f\u0bcd\u0b9f\u0bbf\u0bb2\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bc7 AI use \u0baa\u0ba3\u0bcd\u0ba3\u0bbf \u0b9a\u0bae\u0bcd\u0baa\u0bbe\u0ba4\u0bbf\u0b95\u0bcd\u0b95\u0bb2\u0bbe\u0bae\u0bcd \U0001f4b0\n\n'
            '\u0baf\u0bbe\u0bb0\u0bbf\u0b9f\u0bae\u0bc1\u0bae\u0bcd \u0b95\u0bc7\u0b9f\u0bcd\u0b95 \u0bb5\u0bc7\u0ba3\u0bcd\u0b9f\u0bbe\u0bae\u0bcd. Phone \u0b87\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bbe \u0baa\u0bcb\u0ba4\u0bc1\u0bae\u0bcd.\n\n'
            'ChatGPT, Canva AI \u0baa\u0bcb\u0ba9\u0bcd\u0bb1 10+ tools \u2014 content writing, image creation, freelancing \u2014 \u0b8e\u0bb2\u0bcd\u0bb2\u0bbe\u0bae\u0bc7 \u0b95\u0bb1\u0bcd\u0bb1\u0bc1\u0b95\u0bcd\u0b95\u0bca\u0bb3\u0bcd\u0bb3\u0bb2\u0bbe\u0bae\u0bcd.\n\n'
            '\u0b87\u0ba8\u0bcd\u0ba4 Saturday 6 PM \u2014 1 \u0bae\u0ba3\u0bbf \u0ba8\u0bc7\u0bb0 Live Zoom Workshop. \u0ba4\u0bae\u0bbf\u0bb4\u0bbf\u0bb2\u0bcd.\n\n'
            '\u2705 \u0b87\u0bb2\u0bb5\u0b9a Registration\n'
            '\u2705 \u20b949 \u0bae\u0b9f\u0bcd\u0b9f\u0bc1\u0bae\u0bc7\n'
            '\u2705 No coding needed\n'
            '\u2705 Certificate + Bonuses\n\n'
            'Register FREE \U0001f447'
        ),
        'headline': 'AI \u0b95\u0bb1\u0bcd\u0bb1\u0bc1\u0b95\u0bcd\u0b95\u0bca\u0bb3\u0bcd\u0bb3 \u20b949 \u0baa\u0bcb\u0ba4\u0bc1\u0bae\u0bcd',
        'description': '\u0bb5\u0bc0\u0b9f\u0bcd\u0b9f\u0bbf\u0bb2\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bc7 \u0b9a\u0bae\u0bcd\u0baa\u0bbe\u0ba4\u0bbf\u0baf\u0bc1\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u2014 Live Workshop',
        'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=housewives&utm_content=independence',
    },
    {
        'adset_id': adset_a_id,
        'name': 'Housewives-Value',
        'image_hash': image_hashes[2],
        'message': (
            '\u2615 \u0b92\u0bb0\u0bc1 coffee = \u20b950\n'
            '\U0001f916 AI income skill = \u20b949\n\n'
            '\u0b8e\u0ba4\u0bc1 worth-\u0b86 \u0b87\u0bb0\u0bc1\u0b95\u0bcd\u0b95\u0bc1\u0bae\u0bcd?\n\n'
            '1 \u0bae\u0ba3\u0bbf \u0ba8\u0bc7\u0bb0\u0ba4\u0bcd\u0ba4\u0bbf\u0bb2\u0bcd 10+ AI tools \u0b95\u0bb1\u0bcd\u0bb1\u0bc1\u0b95\u0bcd\u0b95\u0bca\u0bb3\u0bcd\u0bb3\u0bc1\u0b99\u0bcd\u0b95\u0bb3\u0bcd:\n'
            '\u2192 Content creation\n'
            '\u2192 Freelancing opportunities\n'
            '\u2192 Digital product ideas\n\n'
            'Priya, Chennai \u2014 "Workshop-\u0b95\u0bcd\u0b95\u0bc1 \u0b85\u0baa\u0bcd\u0baa\u0bc1\u0bb1\u0bae\u0bcd AI tools use \u0baa\u0ba3\u0bcd\u0ba3\u0bbf \u0bb5\u0bc0\u0b9f\u0bcd\u0b9f\u0bbf\u0bb2\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bc7 earn \u0baa\u0ba3\u0bcd\u0ba3 \u0b86\u0bb0\u0bae\u0bcd\u0baa\u0bbf\u0b9a\u0bcd\u0b9a\u0bc7\u0ba9\u0bcd. Best \u20b949 ever!" \u2b50\u2b50\u2b50\u2b50\u2b50\n\n'
            '\u0b87\u0ba8\u0bcd\u0ba4 Saturday 6 PM. Live Zoom. \u0ba4\u0bae\u0bbf\u0bb4\u0bbf\u0bb2\u0bcd.\n'
            'Register FREE \U0001f447'
        ),
        'headline': '\u20b949 \u2014 Lifetime Income Skill',
        'description': 'Coffee \u0bb5\u0bbf\u0bb2\u0bc8\u0baf\u0bbf\u0bb2\u0bcd AI \u0b95\u0bb1\u0bcd\u0bb1\u0bc1\u0b95\u0bcd\u0b95\u0bca\u0bb3\u0bcd\u0bb3\u0bc1\u0b99\u0bcd\u0b95\u0bb3\u0bcd',
        'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=housewives&utm_content=value',
    },
    # Ad Set B ads
    {
        'adset_id': adset_b_id,
        'name': 'Students-Speed',
        'image_hash': image_hashes[3],
        'message': (
            '60 \u0ba8\u0bbf\u0bae\u0bbf\u0b9f\u0bae\u0bcd. \u0b85\u0bb5\u0bcd\u0bb5\u0bb3\u0bb5\u0bc1 \u0baa\u0bcb\u0ba4\u0bc1\u0bae\u0bcd.\n\n'
            'Coding \u0ba4\u0bc7\u0bb5\u0bc8\u0baf\u0bbf\u0bb2\u0bcd\u0bb2\u0bc8. Degree \u0ba4\u0bc7\u0bb5\u0bc8\u0baf\u0bbf\u0bb2\u0bcd\u0bb2\u0bc8. Phone \u0b87\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bbe \u0baa\u0bcb\u0ba4\u0bc1\u0bae\u0bcd.\n\n'
            '\u0b87\u0ba8\u0bcd\u0ba4 Saturday Live Workshop-\u0bb2\u0bcd:\n'
            '\U0001f916 ChatGPT, Canva AI \u2014 10+ tools live demo\n'
            '\U0001f4b0 AI \u0bae\u0bc2\u0bb2\u0bae\u0bcd earn \u0baa\u0ba3\u0bcd\u0ba3\u0bc1\u0bae\u0bcd 5 methods\n'
            '\U0001f4c4 Resume-\u0b95\u0bcd\u0b95\u0bc1 AI skills add \u0baa\u0ba3\u0bcd\u0ba3\u0bb2\u0bbe\u0bae\u0bcd\n\n'
            'Karthik, Coimbatore \u2014 "College-\u0bb2 \u0baa\u0b9f\u0bbf\u0b95\u0bcd\u0b95\u0bc1\u0bae\u0bcd\u0baa\u0bcb\u0ba4\u0bc7 AI freelancing start \u0baa\u0ba3\u0bcd\u0ba3\u0bbf\u0ba9\u0bc7\u0ba9\u0bcd. Thank you Nirmal sir!" \u2b50\u2b50\u2b50\u2b50\u2b50\n\n'
            '\u20b949 \u0bae\u0b9f\u0bcd\u0b9f\u0bc1\u0bae\u0bc7. Certificate FREE.\n'
            'Register now \U0001f447'
        ),
        'headline': 'College-\u0bb2 \u0baa\u0b9f\u0bbf\u0b95\u0bcd\u0b95\u0bc1\u0bae\u0bcd\u0baa\u0bcb\u0ba4\u0bc7 AI \u0b95\u0bb1\u0bcd\u0b95',
        'description': '60 \u0ba8\u0bbf\u0bae\u0bbf\u0b9f\u0ba4\u0bcd\u0ba4\u0bbf\u0bb2\u0bcd AI-Ready \u0b86\u0b95\u0bc1\u0b99\u0bcd\u0b95\u0bb3\u0bcd',
        'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=students&utm_content=speed',
    },
    {
        'adset_id': adset_b_id,
        'name': 'Students-Fear',
        'image_hash': image_hashes[4],
        'message': (
            '2026-\u0bb2\u0bcd AI \u0ba4\u0bc6\u0bb0\u0bbf\u0baf\u0bbe\u0bae \u0b87\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bbe \u0b95\u0bb7\u0bcd\u0b9f\u0bae\u0bcd.\n\n'
            '\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd competitor AI use \u0baa\u0ba3\u0bcd\u0bb1\u0bbe\u0ba9\u0bcd. \u0ba8\u0bc0\u0b99\u0bcd\u0b95?\n\n'
            '\u0b87\u0ba8\u0bcd\u0ba4 Saturday 6 PM \u2014 1 hour Live Zoom:\n'
            '\u2705 10+ AI tools live demo\n'
            '\u2705 5 earning methods\n'
            '\u2705 Certificate of Completion\n'
            '\u2705 WhatsApp community access\n\n'
            'Deepa, Madurai \u2014 "Workshop-\u0b95\u0bcd\u0b95\u0bc1 \u0b85\u0baa\u0bcd\u0baa\u0bc1\u0bb1\u0bae\u0bcd AI skills \u0b95\u0bb1\u0bcd\u0bb1\u0bc1\u0b95\u0bcd\u0b95\u0bca\u0ba3\u0bcd\u0b9f\u0bc1 earn \u0baa\u0ba3\u0bcd\u0ba3 \u0b86\u0bb0\u0bae\u0bcd\u0baa\u0bbf\u0b9a\u0bcd\u0b9a\u0bc7\u0ba9\u0bcd. Life change \u0b86\u0b9a\u0bcd\u0b9a\u0bc1!" \u2b50\u2b50\u2b50\u2b50\u2b50\n\n'
            '\u0b8e\u0bb2\u0bcd\u0bb2\u0bbe\u0bae\u0bc7 \u0ba4\u0bae\u0bbf\u0bb4\u0bbf\u0bb2\u0bcd. \u20b949 \u0bae\u0b9f\u0bcd\u0b9f\u0bc1\u0bae\u0bc7.\n'
            'Register \U0001f447'
        ),
        'headline': 'AI \u0ba4\u0bc6\u0bb0\u0bbf\u0baf\u0bbe\u0bae \u0b87\u0bb0\u0bc1\u0b95\u0bcd\u0b95\u0bbe\u0ba4\u0bc0\u0b99\u0bcd\u0b95',
        'description': '\u20b949-\u0b95\u0bcd\u0b95\u0bc1 career upgrade \u0baa\u0ba3\u0bcd\u0ba3\u0bc1\u0b99\u0bcd\u0b95\u0bb3\u0bcd',
        'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=students&utm_content=fear',
    },
]

for ad_cfg in ads_config:
    # Create creative
    creative = api_post(f'{AD_ACCOUNT}/adcreatives', {
        'name': f"Creative-{ad_cfg['name']}",
        'object_story_spec': json.dumps({
            'page_id': PAGE_ID,
            'link_data': {
                'image_hash': ad_cfg['image_hash'],
                'link': ad_cfg['link'],
                'message': ad_cfg['message'],
                'name': ad_cfg['headline'],
                'description': ad_cfg['description'],
                'call_to_action': {
                    'type': 'LEARN_MORE',
                    'value': {'link': ad_cfg['link']}
                }
            }
        }),
    })
    creative_id = creative['id']
    
    # Create ad
    ad = api_post(f'{AD_ACCOUNT}/ads', {
        'name': ad_cfg['name'],
        'adset_id': ad_cfg['adset_id'],
        'creative': json.dumps({'creative_id': creative_id}),
        'status': 'PAUSED',
    })
    print(f"  Ad '{ad_cfg['name']}': {ad['id']} (creative: {creative_id})")

# ============================================================
# DONE
# ============================================================
print('\n' + '=' * 50)
print('ALL DONE! Campaign created in PAUSED state.')
print(f'Campaign ID: {campaign_id}')
print(f'Ad Set A (Housewives): {adset_a_id}')
print(f'Ad Set B (Students): {adset_b_id}')
print('=' * 50)
print('\nTo activate: Go to Meta Ads Manager and turn on the campaign.')
print('Or run: python activate_campaign.py')
