"""Update all 4 ad creatives: Saturday -> Sunday"""
import urllib.request, urllib.parse, json

TOKEN = 'EAAUVhY8Tf9YBQ1Kzh9vmq1OdLCogdMwHlOZBGfCCV6NHrZAaqEOnE8gNI1KMeHvh4fgfxVTZAZC1YnPPW9IVoGAklVrx5RjkLwrPBU2csx5oPesXRlfRAsEuKeGS19YrHXLSaCJh4wCmmBQoNNxN1ZCZAXrcE5UdUICWE8euCWILZBn5gDIy45ZBAaVx7NgJRuLZC'
AD_ACCOUNT = 'act_494034697374591'
PAGE_ID = '1455821964711020'

def api_post(endpoint, params):
    params['access_token'] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request('https://graph.facebook.com/v19.0/' + endpoint, data=data, method='POST')
    try:
        return json.loads(urllib.request.urlopen(req).read())
    except Exception as e:
        print('  ERROR:', e.read().decode())
        return None

# --- Ad 1: Housewives-Independence ---
print('Creating new creative for Housewives-Independence...')
c1 = api_post(AD_ACCOUNT + '/adcreatives', {
    'name': 'Housewives-Independence-Sunday',
    'object_story_spec': json.dumps({
        'page_id': PAGE_ID,
        'link_data': {
            'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=housewives&utm_content=independence',
            'message': 'வீட்டிலிருந்தே AI use பண்ணி சம்பாதிக்கலாம் 💰\n\nயாரிடமும் கேட்க வேண்டாம். Phone இருந்தா போதும்.\n\nChatGPT, Canva AI போன்ற 10+ tools — content writing, image creation, freelancing — எல்லாமே கற்றுக்கொள்ளலாம்.\n\nஇந்த Sunday 6 PM — 1 மணி நேர Live Zoom Workshop. தமிழில்.\n\n✅ இலவச Registration\n✅ ₹49 மட்டுமே\n✅ No coding needed\n✅ Certificate + Bonuses\n\nRegister FREE 👇',
            'name': 'AI கற்றுக்கொள்ள ₹49 போதும்',
            'description': 'வீட்டிலிருந்தே சம்பாதியுங்கள் — Live Workshop',
            'image_hash': 'c8069c23fef1e04c95d0aaee38f4113b',
            'call_to_action': {'type': 'LEARN_MORE', 'value': {'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=housewives&utm_content=independence'}},
        }
    }),
})
print('  Creative:', c1)

# --- Ad 2: Housewives-Value ---
print('Creating new creative for Housewives-Value...')
c2 = api_post(AD_ACCOUNT + '/adcreatives', {
    'name': 'Housewives-Value-Sunday',
    'object_story_spec': json.dumps({
        'page_id': PAGE_ID,
        'link_data': {
            'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=housewives&utm_content=value',
            'message': '☕ ஒரு coffee = ₹50\n🤖 AI income skill = ₹49\n\nஎது worth-ஆ இருக்கும்?\n\n1 மணி நேரத்தில் 10+ AI tools கற்றுக்கொள்ளுங்கள்:\n→ Content creation\n→ Freelancing opportunities\n→ Digital product ideas\n\nPriya, Chennai — "Workshop-க்கு அப்புறம் AI tools use பண்ணி வீட்டிலிருந்தே earn பண்ண ஆரம்பிச்சேன். Best ₹49 ever!" ⭐⭐⭐⭐⭐\n\nஇந்த Sunday 6 PM. Live Zoom. தமிழில்.\nRegister FREE 👇',
            'name': '₹49 — Lifetime Income Skill',
            'description': 'Coffee விலையில் AI கற்றுக்கொள்ளுங்கள்',
            'image_hash': '3530d9182b393bb1b3dbe5f8d45e00da',
            'call_to_action': {'type': 'LEARN_MORE', 'value': {'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=housewives&utm_content=value'}},
        }
    }),
})
print('  Creative:', c2)

# --- Ad 3: Students-Speed ---
print('Creating new creative for Students-Speed...')
c3 = api_post(AD_ACCOUNT + '/adcreatives', {
    'name': 'Students-Speed-Sunday',
    'object_story_spec': json.dumps({
        'page_id': PAGE_ID,
        'link_data': {
            'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=students&utm_content=speed',
            'message': '60 நிமிடம். அவ்வளவு போதும்.\n\nCoding தேவையில்லை. Degree தேவையில்லை. Phone இருந்தா போதும்.\n\nஇந்த Sunday Live Workshop-ல்:\n🤖 ChatGPT, Canva AI — 10+ tools live demo\n💰 AI மூலம் earn பண்ணும் 5 methods\n📄 Resume-க்கு AI skills add பண்ணலாம்\n\nKarthik, Coimbatore — "College-ல படிக்கும்போதே AI freelancing start பண்ணினேன். Thank you Nirmal sir!" ⭐⭐⭐⭐⭐\n\n₹49 மட்டுமே. Certificate FREE.\nRegister now 👇',
            'name': 'College-ல படிக்கும்போதே AI கற்க',
            'description': '60 நிமிடத்தில் AI-Ready ஆகுங்கள்',
            'image_hash': '49316a5f6c9a5b9b19bfb8330b5f8fb3',
            'call_to_action': {'type': 'LEARN_MORE', 'value': {'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=students&utm_content=speed'}},
        }
    }),
})
print('  Creative:', c3)

# --- Ad 4: Students-Fear ---
print('Creating new creative for Students-Fear...')
c4 = api_post(AD_ACCOUNT + '/adcreatives', {
    'name': 'Students-Fear-Sunday',
    'object_story_spec': json.dumps({
        'page_id': PAGE_ID,
        'link_data': {
            'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=students&utm_content=fear',
            'message': '2026-ல் AI தெரியாம இருந்தா கஷ்டம்.\n\nஉங்கள் competitor AI use பண்றான். நீங்க?\n\nஇந்த Sunday 6 PM — 1 hour Live Zoom:\n✅ 10+ AI tools live demo\n✅ 5 earning methods\n✅ Certificate of Completion\n✅ WhatsApp community access\n\nDeepa, Madurai — "Workshop-க்கு அப்புறம் AI skills கற்றுக்கொண்டு earn பண்ண ஆரம்பிச்சேன். Life change ஆச்சு!" ⭐⭐⭐⭐⭐\n\nஎல்லாமே தமிழில். ₹49 மட்டுமே.\nRegister 👇',
            'name': 'AI தெரியாம இருக்காதீங்க',
            'description': '₹49-க்கு career upgrade பண்ணுங்கள்',
            'image_hash': 'dceffd9debd94aad7c6a5c6f437b2dba',
            'call_to_action': {'type': 'LEARN_MORE', 'value': {'link': 'https://ai-money-earning.vercel.app/ta/?utm_source=meta&utm_medium=paid&utm_campaign=students&utm_content=fear'}},
        }
    }),
})
print('  Creative:', c4)

# --- Step 5: Update ads with new creatives ---
print('\nUpdating ads with new creatives...')

if c1 and c1.get('id'):
    r = api_post('6951801143868', {'creative': json.dumps({'creative_id': c1['id']})})
    print('  Housewives-Independence -> ' + c1['id'] + ':', r)

if c2 and c2.get('id'):
    r = api_post('6951801152468', {'creative': json.dumps({'creative_id': c2['id']})})
    print('  Housewives-Value -> ' + c2['id'] + ':', r)

if c3 and c3.get('id'):
    r = api_post('6951039894868', {'creative': json.dumps({'creative_id': c3['id']})})
    print('  Students-Speed -> ' + c3['id'] + ':', r)

if c4 and c4.get('id'):
    r = api_post('6951039903268', {'creative': json.dumps({'creative_id': c4['id']})})
    print('  Students-Fear -> ' + c4['id'] + ':', r)

print('\nDONE! All 4 ads updated to Sunday.')
