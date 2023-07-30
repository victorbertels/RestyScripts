#PAM SCRIPT Employees

# fix the CL with the correct Menu levels
account = '5e81f14758168e0001d981d5'
location = '5f6e0f7283d1e22030a59912'
query ={'account' : account, 'location': location}

links = pcli.channelLinks.list_all(q=query)


for link in links:
    pcli.channelLinks.update(link, {'posSettings.simphony.itemMenuLevel' : 1,'posSettings.simphony.itemSubLevel': 3 })





#Fix the locations with the correct menu levels
account = '5e81f14758168e0001d981d5'
location = '5f0830509f26c0077d566597'
query ={'account' : account, '_id': location}

links = pcli.locations.list_all(q=query)


for link in links:
    pcli.locations.update(link, {'posSettings.simphony.itemMenuLevel' : 1,'posSettings.simphony.itemSubLevel': 3 })

# Enable Discounts everywhere
account = '5e81f14758168e0001d981d5'

query ={'account' : account}

links = pcli.channelLinks.list_all(q=query)



for link in links:
    pcli.channelLinks.update(link, {'channelSettings.sendDiscount': True})




################################################################################################################
for link in links:
    channel =   link.get('channel')
    if channel == 9:
        pcli.channelLinks.update(link,{"posSettings.simphony.employeeObjectNumber": "8954"})
    elif channel == 7:
        pcli.channelLinks.update(link,{"posSettings.simphony.employeeObjectNumber": "8955"})
    elif channel == 2:
        pcli.channelLinks.update(link,{"posSettings.simphony.employeeObjectNumber": "8932"})
    elif channel == 10005:
        pcli.channelLinks.update(link,{"posSettings.simphony.employeeObjectNumber": "8963"})

#PAM SCRIPT Discounts
query ={'account' : '5e81f14758168e0001d981d5'}

links = pcli.channelLinks.list_all(q=query)

for link in links:
    channel =   link.get('channel')
    if channel == 9:
        pcli.channelLinks.update(link,{"posSettings.simphony.discountId": "826002002"})
    elif channel == 2:
        pcli.channelLinks.update(link,{"posSettings.simphony.discountId": "826002002"})
    elif channel == 7:
        pcli.channelLinks.update(link,{"posSettings.simphony.discountId": "826002002"})
    elif channel == 1:
        pcli.channelLinks.update(link,{"posSettings.simphony.discountId": "826002002"})  
    elif channel == 10005:
        pcli.channelLinks.update(link,{"posSettings.simphony.discountId": "826002001"})

query ={'account' : '5e81f14758168e0001d981d5'}
links = pcli.channelLinks.list_all(q=query)

for link in links:
    channel =   link.get('channel')
    if channel == 9:
        pcli.channelLinks.update(link,{"posSettings.simphony.bufferOrders": False})
    elif channel == 2:
        pcli.channelLinks.update(link,{"posSettings.simphony.bufferOrders": False})
    elif channel == 7:
        pcli.channelLinks.update(link,{"posSettings.simphony.bufferOrders": False})
    elif channel == 1:
        pcli.channelLinks.update(link,{"posSettings.simphony.bufferOrders": False})



      "bufferOrders": true,
