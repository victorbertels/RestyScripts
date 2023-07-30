#PAM Employees


whole_acc_query = {'account' : '5e7bbf7265013b00010cb6aa'}
env = pcli
links = env.channelLinks.list_all(q=whole_acc_query)
for link in links:
    channel = link.get('channel')
    if channel == 1:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.checkIdTemplate": "{orderId}"
            
        })
    elif channel == 2:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.checkIdTemplate": "{orderId}",
            
        })
    elif channel == 7:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.checkIdTemplate": "{customerName}",
            "posSettings.simphony.orderNoteTemplate":"{displayOrderId}",

            "channelSettings.orderNoteTemplate": "{orderNote}",
            
        })

    elif channel == 26:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.pCheckInfoLinesTemplate": "{orderId} , {orderNote}",
            "posSettings.simphony.orderNoteTemplate": "{displayOrderId}",
            "posSettings.simphony.checkIdTemplate": "{customerName}",
        })

    elif channel == 12:
            pcli.channelLinks.update(link,{
            "posSettings.simphony.pCheckInfoLinesTemplate": "{orderId} , {orderNote}",
            "posSettings.simphony.orderNoteTemplate": "{displayOrderId}",
            "posSettings.simphony.checkIdTemplate": "{customerName}",
            
        })