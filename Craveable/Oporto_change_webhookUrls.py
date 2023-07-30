payload = {"channelSettings": {
                "courierUpdateURL": "https://api.oporto.com.au/deliverect/webhooks/order/courier",
                "updatePrepTimeURL": "https://api.oporto.com.au/deliverect/webhooks/order/prep-time",
                "statusUpdateURL": "https://api.oporto.com.au/deliverect/webhooks/order/status",
                "busyModeURL": "https://api.oporto.com.au/deliverect/webhooks/busy-mode",
                "snoozeUnsnoozeURL": "https://api.oporto.com.au/deliverect/webhooks/menu/snooze-products",
                "menuUpdateURL": "https://api.oporto.com.au/deliverect/webhooks/menu",
                "activateURL": "https://api.oporto.com.au/deliverect/webhooks/channel/status"
}}

exclude_locations= [
"5f109866f3494b8ce30aaa56",
"633276b8c0b6239ce87d7f2b",
"632aa2e1143f055c05b31c1e",
"60bf8ee4095b2bdf543501b4",]


channels = pcli.channelLinks.list_all(q={"account" : "5e7bbf7265013b00010cb6aa" , "channel" : 10220})
for channel in channels: 
    if channel.location not in exclude_locations:
        print(channel.channelSettings.courierUpdateURL)
        print(channel.channelSettings.updatePrepTimeURL)
        print(channel.channelSettings.statusUpdateURL)
        print(channel.channelSettings.busyModeURL)
        print(channel.channelSettings.snoozeUnsnoozeURL)
        print(channel.channelSettings.menuUpdateURL)
        print(channel.channelSettings.activateURL)
        # print(channel.location)
        pcli.channelLinks.update(channel,payload)

