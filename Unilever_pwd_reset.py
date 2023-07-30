import requests
import json

user_list = ["bpglenquarie@gmail.com",
"BudgetCampsie@riadpetroleum.com.au",
"Khassawneh@hotmail.com",
"evlemp@hotmail.com",
"dimi79@live.com",
"harry@captainshop.com.au",
"bp887766@gmail.com",
"bp3@bigpond.com",
"Dinesh.Jeshani@ge.com",
"bpwilloughby@bigpond.com",
"bp3@bigpond.com",
"khassawneh@hotmail.com",
"zhangjinfang@goldensquaregroup.com.au",
"george.makhlouf@hotmail.com",
"be2212@jasbe.com.au",
"sagar_hirani@ymail.com",
"Info@bigbunz.com.au",
"foodworksrozelle@gmail.com",
"Khassawneh@hotmail.com",
"budgetpetersham@hotmail.com",
"sales@metroavalon.com.au",
"Westsidelidcombe@gmail.com",
"admin@shreejiholdings.com",
"admin@fairwayinvest.com.au",
"Info@bigbunz.com.au",
"hkamel@hotmail.com.au",
"nizam.shakti@gmail.com",
"functions@waterfrontstore.com.au",
"jeleftheriou@bigpond.com",
"madtoppings@outlook.com",
"madtoppings@outlook.com",
"madtoppings@outlook.com",
"unigashomebush@gmail.com",
"hallanis7days@gmail.com",
"maridaleparknews@gmail.com",
"hiren2012@hotmail.com",
"milton@nightowl.com.au",
"ashgrovewest@nightowl.com.au",
"Yangpu0920@gmail.com",
"mystore1634@gmail.com",
"Rizkinvestments@bigpond.com",
"Fitzgibbon@nightowl.com.au",
"hollandpark@nightowl.com.au",
"freedomsouthport@outlook.com",
"indooroopilly@nightowl.com.au",
"Littlemountain@nightowl.com.au",
"nightowl4509@gmail.com",
"igamudgee@gmail",
"fernbrooke@nightowl.com.au",
"Southport@nightowl.com.au",
"tarragindi@nightowl.com.au",
"Windsor@nightowl.com.au",
"info@wurtullaiga.com.au",
"narangba@bunney-s.com.au",
"redcliffe@unitrade-iga.com.au",
"clontarf@unitrade-iga.com.au",
"boondall@nightowl.com.au",
"igaxpressmichelton@gmail.com",
"VinayGaind1969@yahoo.com.au",
"shelltingalpa9@gmail.com",
"kangaroopoint@nightowl.com.au",
"Mermaidbeach@nightowl.com.au",
"adamphope@hotmail.com",
"libertymargate9268@gmail.com",
"enoggera@nightowl.com.au",
"bpstafford475@gmail.com",
"farmmartov@gmail.com",
"liberty4113@gmail.com",
"essendon.smokinjoes@outlook.com.au",
"nysha_bp@yahoo.com",
"bpflemington@grouppinnacle.com.au",
"bpstationvale@grouppinnacle.com.au",
"PAKENHAM@NUVPETROLEUM.COM",
"PAKENHAM@NUVPETROLEUM.COM",
"langwarrin@nuvpetroleum.com",
"nezarsaleh@hotmail.com",
"rowville@nuvpetroleum.com",
"TREMONT@NUVPETROLEUM.COM.AU",
"RESERVOIR@NUVPETROLEUM.COM",
"zhuangzhu5168@gmail.com",
"naivedyamptyltd@gmail.com",
"bpblackburn@grouppinnacle.com.au",
"san_bp@yahoo.com",
"bossgeelongacc@gmail.com",
"bossgeelongacc@gmail.com",
"bossgeelongacc@gmail.com",]




user_ids = pcli.users.list_all(q={'email' : {"$in" :user_list}})

for user_id in user_ids:
    _id = user_id._id
    etag = user_id._etag
    print(_id)
    url = f"https://api.deliverect.com/v1/user/{_id}/resetPassword"
    print(url)

    payload = json.dumps({
    "email": "victor.bertels@deliverect.com"
    })
    headers = {
    'If-Match': f'{etag}',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NTI5NjUzODIsImV4cCI6MTY1MzA1MTc4MiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.jddYilqSWguA6Hp7DXFqL7jErQM87X27CLNQauTiig_8JOBAmPbqi3U6GnJvbmBH8QF77eEs8gjxYiPe-xIHK7R5RGo1jHTJOA-S3DocOfb1xTegX2Z-qTVxYAvNc3nFaFBsZpw3xkZL71AK-0E5do0_EBHEh2PlqquWyVTKLOq9__JRPJM7Zdf5Vf5MTlbyvY5OXYSlKL8vlOKN1byMt1utunYzwoKqOgnqJmlhAYlwl3SfoETeyYCj6e5vnDCalFzOa67cy-K7fYrVVr3LSfGUoF6uDeV9e9j2cyZsgvwn60FGVjPsP2Dz2DQlgeeUX4gdSWEoN90AKakpyw41Xg',
  'Content-Type': 'application/json'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

