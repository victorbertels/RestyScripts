CHANNEL = 19


query = pcli.channelLinks.list_all(q={"channel" : CHANNEL})


for clink in query:
    location = pcli.locations.get(clink.location)
    print(f"Channel Link name : {clink.name} -{clink._id} -Location name: {location.name}, ID: {location._id}")