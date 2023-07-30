from asyncore import write
from itertools import groupby
import collections
import json
import datetime 



f= open(f"RR-1233.csv" , "w+")
f.write("Location,Store,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday\n")


channelLinkMenus = {}
menus = pcli.channelMenus.list_all(q={"account":"5fe17b1effe9e99933f9f58a"})
channelLinks = pcli.channelLinks.list_all(q={"account": "5fe17b1effe9e99933f9f58a"})
channelLinksById = {channelLink._id: channelLink for channelLink in channelLinks}
locations = pcli.locations.list_all(q={"account": "5fe17b1effe9e99933f9f58a"})
locationsById = {location._id: location for location in locations}
locationChannelLinks = collections.defaultdict(list)
for channelLink in channelLinks:
  locationChannelLinks[channelLink.get("location")].append(channelLink)
for menu in menus:
  for channelLinkId in menu.get("activeChannelLinkIds", []):
    channelLinkMenus[channelLinkId]=menu.get("_id")


availabilities = pcli.menuAvailabilities.list_all(q={"account":"5fe17b1effe9e99933f9f58a"})
availabilitiesPerMenuLoc = collections.defaultdict(lambda: collections.defaultdict(list))
for avail in availabilities:
  availabilitiesPerMenuLoc[(avail.menu, avail.location)][avail.dayOfWeek].append((avail.startTime, avail.endTime))

for locationId in locationChannelLinks:
  location = locationsById.get(locationId)
  for channelLink in locationChannelLinks.get(locationId):
    menuId = channelLinkMenus.get(channelLink._id)
    if not menuId:
      # channellink does not ahve an active menu
      continue
    avails = availabilitiesPerMenuLoc.get((menuId, location._id))
    if not avails:
      print(f"{location.name} - {menuId} has no availabilities")
      continue
    
    cells = []
    cells.append(location.name)
    cells.append(channelLink.name)
    # print("channelLinksName: " ,channelLink.name)
    # print(cells)
    for day in range(1, 8):
      timeslots = avails.get(day)
      if not timeslots:
        cells.append("")
      else:
        cells.append(" ".join([f"{t[0]}-{t[1]}" for t in timeslots]))
    print(cells)

    f.write(",".join(cells)+"\n")


f.close()




# f= open(f"RedRooster.csv" , "w+")
# f.write("Location,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday\n")
# for i in query:
#   location = i.location
#   location_name = pcli.locations.get(location).name
#   print(location_name)
#   get_availabilities = pcli.menuAvailabilities.list_all(q={"account" : "5fe17b1effe9e99933f9f58a" ,"menu" : "6229337b8b7452f13f81b4c3" ,"location" : location})

#   grouped = {group[0]: [(entry.get("startTime"), entry.get("endTime")) for entry in group[1]] for group in groupby(get_availabilities, key=lambda x: x.get("dayOfWeek"))}
#   #print(grouped.get(1))

  
#   cells = [location_name]
#   for daynum in range(1,8):
#     cells.append(" ".join([f"{timeslot[0]}-{timeslot[1]}" for timeslot in grouped.get(daynum)]))
#   f.write(",".join(cells)+"\n")
# f.close()



#   # "RR123466":{"1":["12:00" , "21:00"]}
 





