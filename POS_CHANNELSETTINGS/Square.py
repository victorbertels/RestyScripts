



###EPOS_NOW
from collections import Counter

pageCount = 1
listOfSettings = []
while True:
  links = pcli.channelLinks.list(q={'posSystemId': 48} , page = pageCount)
  # links = pcli.channelLinks.list_all(q={'posSystemId': 48})

  pageCount += 1
  print(pageCount)
  listOfSettings.append(links)
  # print(listOfSettings)
  if pageCount == 2:
    
  # if links == []:
    print("end of the pages")
    
    skeys = set()
    print(listOfSettings)
    for link in listOfSettings:
      for key in link.posSettings.get("simphony_gen2",{}).keys():
        # print(key)
        skeys.add(key)

    # print(skeys)

      data = {}
      for key in skeys:
          data[key] = Counter(bool(l.posSettings.get('simphony_gen2', {}).get(key)) for l in links)


      print(data)
      break

  


  skeys = set()
  for link in listOfSettings:
    for key in link.posSettings.get("dma",{}).keys():
      # print(key)
      skeys.add(key)

  # print(skeys)

  data = {}
  for key in skeys:
      data[key] = Counter(bool(l.posSettings.get('dma', {}).get(key)) for l in links)


  print(data)