locs = pcli.locations.list_all(q={"posSystemId": 25,'posSettings.kounta.logOps':False})


for i in locs:
    pcli.locations.update(i,{
        'posSettings.kounta.logOps' : True
    },propagate='all', override=1)