#PAM SCRIPT Discounts
query ={'account' : '5e81f14758168e0001d981d5'}
#, "channelSettings.sendDiscount" : False
links = pcli.channelLinks.list_all(q=query)

for link in links:
    print(link.posSettings.simphony.discountId)
    pcli.channelLinks.update(link,{
        "channelSettings" : {'sendDiscount':True}
    })
    channel =   link.get('channel')
    
    if channel == 7:
        pcli.channelLinks.update(link,{"posSettings":{"simphony":{"discountId": "826002002"}}})
    elif channel == 2:
        pcli.channelLinks.update(link,{"posSettings":{"simphony":{"discountId": "826002002"}}})
    elif channel == 1:
        pcli.channelLinks.update(link,{"posSettings":{"simphony":{"discountId": "826002002"}}})  
    elif channel == 10005:
        pcli.channelLinks.update(link,{"posSettings":{"simphony":{"discountId": "826002001"}}})
    elif channel == 9:
        pcli.channelLinks.update(link,{"posSettings":{"simphony":{"discountId": "826002002"}}})


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

