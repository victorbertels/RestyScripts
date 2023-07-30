links = pcli.channelLinks.list_all(q={'posSystemId' : 1})

from collections import Counter

skeys = set()
for link in links:
  for key, value in link.posSettings.get("lightspeed",{}).items():
      if key == "bagFeePLU" and value == True:
          print(link)
      skeys.add(key)

data = {}
for key in skeys:
     data[key] = Counter(bool(l.posSettings.get('lightspeed', {}).get(key)) for l in links)


data
'''------------------------------------------------''' 
links = pcli.channelLinks.list_all(q={'posSystemId' : 1})

from collections import Counter

skeys = set()
for link in links:
  for key, value in link.posSettings.get("lightspeed",{}).items():
      if key == "paymentTypeId_paymentTypeTypeId" and value == True:
          print(link)
      skeys.add(key)

data = {}
for key in skeys:
     data[key] = Counter(str(l.posSettings.get('lightspeed', {}).get(key)) for l in links)
 

data



###EPOS_NOW
links = pcli.channelLinks.list_all(q={'posSystemId': 2})

skeys = set()
for link in links:
  for key in link.posSettings.get("epos_now",{}).keys():
    print(key)
    skeys.add(key)

print(skeys)

data = {}
for key in skeys:
     data[key] = Counter(bool(l.posSettings.get('epos_now', {}).get(key)) for l in links)


data
