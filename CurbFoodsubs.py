denmark = '60b4d6577a1494c0d93638d9'
sweden = '60f686ea7ce019a52122d711'
germany = '619d949292c19e0d28192b5f'

all_of_them = [sweden]

query = pcli.channelLinks.list_all(q={'account':{"$in":all_of_them}})
Locquery = pcli.locations.list_all(q={'account':{"$in":all_of_them}})


'''
for i in Locquery:
    print(i.subscriptions)
'''

for i in query:
    print(i.tags)
    print(i.subscriptions)