query = pcli.channelLinks.list_all(q={"account" : {"$in" : List}})
query2 = pcli.channelLinks.list_all(q={"account" : {"$in" : list2}})


channelLinks = {}

for acc in query:
    channelNum = acc.channel
    if channelNum == 7:
        try:
            channelNum = acc.channel
            app = acc.channelSettings.application
            if channelNum == 7:
                channelLinks[acc._id] = str(app)
        except:

            channelLinks[acc._id] = "no app"


for acc in query2:
    channelNum = acc.channel
    if channelNum == 7:
        try:
            channelNum = acc.channel
            app = acc.channelSettings.application
            if channelNum == 7:
                channelLinks[acc._id] = str(app)
        except:

            channelLinks[acc._id] = "no app"


print(channelLinks)



sorted_footballers_by_goals = sorted(channelLinks.items(), key=lambda x:x[1])