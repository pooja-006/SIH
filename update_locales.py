import json

translations = {
    "Andaman and Nicobar Islands": {"en": "Andaman and Nicobar Islands", "hi": "अंडमान और निकोबार द्वीप समूह", "gu": "આંદામાન અને નિકોબાર ટાપુઓ"},
    "Andhra Pradesh": {"en": "Andhra Pradesh", "hi": "आंध्र प्रदेश", "gu": "આંધ્ર પ્રદેશ"},
    "Assam": {"en": "Assam", "hi": "असम", "gu": "આસામ"},
    "Bihar": {"en": "Bihar", "hi": "बिहार", "gu": "બિહાર"},
    "Chandigarh": {"en": "Chandigarh", "hi": "चंडीगढ़", "gu": "ચંડીગઢ"},
    "Chhattisgarh": {"en": "Chhattisgarh", "hi": "छत्तीसगढ़", "gu": "છત્તીસગઢ"},
    "Delhi": {"en": "Delhi", "hi": "दिल्ली", "gu": "દિલ્હી"},
    "Goa": {"en": "Goa", "hi": "गोवा", "gu": "ગોવા"},
    "Gujarat": {"en": "Gujarat", "hi": "गुजरात", "gu": "ગુજરાત"},
    "Himachal Pradesh": {"en": "Himachal Pradesh", "hi": "हिमाचल प्रदेश", "gu": "હિમાચલ પ્રદેશ"},
    "Jammu and Kashmir": {"en": "Jammu and Kashmir", "hi": "जम्मू और कश्मीर", "gu": "જમ્મુ અને કાશ્મીર"},
    "Jharkhand": {"en": "Jharkhand", "hi": "झारखंड", "gu": "ઝારખંડ"},
    "Karnataka": {"en": "Karnataka", "hi": "कर्नाटक", "gu": "કર્ણાટક"},
    "Kerala": {"en": "Kerala", "hi": "केरल", "gu": "કેરળ"},
    "Madhya Pradesh": {"en": "Madhya Pradesh", "hi": "मध्य प्रदेश", "gu": "મધ્ય પ્રદેશ"},
    "Maharashtra": {"en": "Maharashtra", "hi": "महाराष्ट्र", "gu": "મહારાષ્ટ્ર"},
    "Manipur": {"en": "Manipur", "hi": "मणिपुर", "gu": "મણિપુર"},
    "Meghalaya": {"en": "Meghalaya", "hi": "मेघालय", "gu": "મેઘાલય"},
    "Odisha": {"en": "Odisha", "hi": "ओडिशा", "gu": "ઓડિશા"},
    "Rajasthan": {"en": "Rajasthan", "hi": "राजस्थान", "gu": "રાજસ્થાન"},
    "Tamil Nadu": {"en": "Tamil Nadu", "hi": "तमिलनाडु", "gu": "તમિલનાડુ"},
    "Telangana": {"en": "Telangana", "hi": "तेलंगाना", "gu": "તેલંગાણા"},
    "Tripura": {"en": "Tripura", "hi": "त्रिपुरा", "gu": "ત્રિપુરા"},
    "Uttar Pradesh": {"en": "Uttar Pradesh", "hi": "उत्तर प्रदेश", "gu": "ઉત્તર પ્રદેશ"},
    "Uttarakhand": {"en": "Uttarakhand", "hi": "उत्तराखंड", "gu": "ઉત્તરાખંડ"},
    "West Bengal": {"en": "West Bengal", "hi": "पश्चिम बंगाल", "gu": "પશ્ચિમ બંગાળ"}
}

import os
path = "frontend/src/locales/"
for lang in ["en", "hi", "gu"]:
    filepath = os.path.join(path, f"{lang}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for state, trans in translations.items():
        data["options"][state] = trans[lang]
        
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Done")
