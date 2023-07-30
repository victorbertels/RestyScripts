#PAM Employees


whole_acc_query = {'account' : '5e81f14758168e0001d981d5'}
some_loc_query = {'account' : '5e81f14758168e0001d981d5',"location" :{"$in" : ["60b4c3b8eceef973e2f4ef77","60b4c39329101cc2c0abd4a9"] }}
one_loc_query = {'account' : "5e81f14758168e0001d981d5" , 'location' : '5fb4ef44e9145d3df6c86ee9'}
env = pcli
links = env.channelLinks.list_all(q=one_loc_query)
for link in links:
    channel = link.get('channel')
    if channel == 1:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.employeeObjectNumber": "7860"
            
        })
    elif channel == 2:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.employeeObjectNumber": "8932"
            
        })
    elif channel == 7:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.employeeObjectNumber": "8955"
            
        })

    elif channel == 9:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.employeeObjectNumber": "8954"
            
        })
    elif channel == 10005:
        pcli.channelLinks.update(link,{
            "posSettings.simphony.employeeObjectNumber": "8963"
            
        })
