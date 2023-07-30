# Wendy's Prod update to 15000 TAX


query = pcli.locations.list_all(q={'account':'603fa3225de02e8e2fd835d5'})


for i in query: 
    pcli.locations.update(i,{
        "posSettings":{"ncr":{
        "defaultTakeawayTax": "15000",
        "defaultDeliveryTax":"15000"}}})



query = pcli.channelLinks.list_all(q={'account':'603fa3225de02e8e2fd835d5'})


for i in query: 
    pcli.channelLinks.update(i,{
        "posSettings":{"ncr":{
        "defaultTakeawayTax": "15000",
        "defaultDeliveryTax":"15000"}}})