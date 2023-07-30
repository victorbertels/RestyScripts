query ={'account' : '5e9eef1bc766d30001c6294c'}
links = pcli.locations.list_all(q=query,only= 'posSettings.simphony.serverEndpoint')
for link in links:
    pcli.locations.update(link,{  "productLocation": "5e9eef27c766d30001c62953"}, propagate ='all')
    

