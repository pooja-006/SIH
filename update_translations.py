import json
import os
for lang in ['en', 'hi', 'gu']:
    filepath = os.path.join('frontend/src/locales/', f'{lang}.json')
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if 'signin' not in data:
        data['signin'] = {}
    
    data['signin']['create_account'] = 'Create Account' if lang == 'en' else 'खाता बनाएँ' if lang == 'hi' else 'ખાતું બનાવો'
    data['signin']['account_exists'] = 'Account already exists' if lang == 'en' else 'खाता पहले से मौजूद है' if lang == 'hi' else 'ખાતું પહેલેથી જ અસ્તિત્વમાં છે'
    data['signin']['register_button'] = 'Register' if lang == 'en' else 'पंजीकरण करें' if lang == 'hi' else 'નોંધણી કરો'
    data['signin']['back_to_login'] = 'Back to Sign In' if lang == 'en' else 'साइन इन पर वापस' if lang == 'hi' else 'સાઇન ઇન પર પાછા ફરો'
    data['signin']['success'] = 'Account created successfully' if lang == 'en' else 'खाता सफलतापूर्वक बनाया गया' if lang == 'hi' else 'ખાતું સફળતાપૂર્વક બનાવવામાં આવ્યું'
    data['signin']['network_error'] = 'Network error' if lang == 'en' else 'नेटवर्क त्रुटि' if lang == 'hi' else 'નેટવર્ક ભૂલ'
    data['signin']['invalid_email'] = 'Invalid email' if lang == 'en' else 'अमान्य ईमेल' if lang == 'hi' else 'અમાન્ય ઈમેલ'
    data['signin']['server_error'] = 'Server error' if lang == 'en' else 'सर्वर त्रुटि' if lang == 'hi' else 'સર્વર ભૂલ'
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
