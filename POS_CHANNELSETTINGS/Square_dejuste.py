from collections import Counter

links = pcli.locations.list_all(q={'posSystemId' : 13})


skeys = set()
for link in links:
  for key in link.posSettings.get("square",{}).keys():
#     print(key)
    skeys.add(key)

data = {}
for key in skeys:
     data[key] = Counter(bool(l.posSettings.get('square', {}).get(key)) for l in links)
data



'''------------------------------------------------''' 
links = pcli.channelLinks.list_all(q={'posSystemId' : 20000})

from collections import Counter

skeys = set()
for link in links:
  for key, value in link.posSettings.get("dma",{}).items():
      if key == "paymentTypeId_paymentTypeTypeId" and value == True:
          print(link)
      skeys.add(key)

data = {}
for key in skeys:
     data[key] = Counter(str(l.posSettings.get('lightspeed', {}).get(key)) for l in links)
 

data



###Square
links = pcli.channelLinks.list_all(q={'posSystemId': 15})

skeys = set()
for link in links:
  for key in link.posSettings.get("square",{}).keys():
    print(key)
    skeys.add(key)

print(skeys)

data = {}
for key in skeys:
     data[key] = Counter(bool(l.posSettings.get('square', {}).get(key)) for l in links)


data


###TouchBistro
links = pcli.channelLinks.list_all(q={'posSystemId': 20000})

from collections import Counter

skeys = set()
for link in links:
  for key in link.posSettings.get("dma",{}).keys():
    print(key)
    skeys.add(key)

print(skeys)

data = {}
for key in skeys:
     data[key] = Counter(bool(l.posSettings.get('dma', {}).get(key)) for l in links)


data