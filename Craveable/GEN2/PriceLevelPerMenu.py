## Chicken Treat
query = pcli.channelLinks.list_all(q={"account" : "63290d3fdceae416df65c7e8" , "location" : "636055a2cb9fccb436a3e76c"})

for channel in query:
    pcli.channelLinks.update(channel,{
         "priceLevelSettings": {
                    "takeaway": "1",
                    "delivery": "2",
                    "eatIn": "1"
    }
    })


#Oporto 
query = pcli.channelLinks.list_all(q={"account" : "63435e96e54f9c12e91c9745"})

for channel in query:
    pcli.channelLinks.update(channel,{
         "priceLevelSettings": {
                    "takeaway": "1",
                    "delivery": "2",
                    "eatIn": "1"
    }
    })

#Red Rooster 
query = pcli.channelLinks.list_all(q={"account" : "63d9cbe3301774db888211ca"})

for channel in query:
    pcli.channelLinks.update(channel,{
         "priceLevelSettings": {
                    "takeaway": "1",
                    "delivery": "2",
                    "eatIn": "1"
    }
    })


# temporary disable for chicken Treat untill dev is done

query = pcli.channelLinks.list_all(q={"account" : "63290d3fdceae416df65c7e8"})

for channel in query:
    pcli.channelLinks.update(channel,{
         "priceLevelSettings": {}
    })


# temporary disable for Oporto  untill dev is done
query = pcli.channelLinks.list_all(q={"account" : "63435e96e54f9c12e91c9745"})

for channel in query:
    pcli.channelLinks.update(channel,{
         "priceLevelSettings": {}
    })


## Chicken Treat v2
query = pcli.channelLinks.list_all(q={"account" : "640fb7c8418a81f080a5a8a2" , "location" : "640fb830b1cabeb0dc1a85d5"})

for channel in query:
    pcli.channelLinks.update(channel,{
         "priceLevelSettings": {
                    "takeaway": "1",
                    "delivery": "2",
                    "eatIn": "1"
    }
    })
