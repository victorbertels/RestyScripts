#Get data from account

for i in locations: 
  number_of_channelLinks = len(i.channelLinks)
  acc_name= pcli.accounts.get(i.account)
  print(acc_name.name,"-",acc_name._id)
  print('location :',i.name,)
  print(number_of_channelLinks,' channelLinks')
  print("---------------------------------------------")




number = 32
accounts = pcli.accounts.list_all(q={'posSystem':number},only='name')
locations = pcli.locations.list_all(q={'posSystemId':number})
CL = pcli.channelLinks.list_all(q={"posSystemId":number})


for i in locations:
    number_of_channelLinks = len(i.channelLinks)
    print(number_of_channelLinks)
    acc_name = accounts.name
    print(acc_name)




###Talabat
CL_query = pcli.channelLinks.list_all(q={'channel' : 20})
for i in CL_query:
  loc = i.location
  acc = i.account
  loc_query = pcli.locations.get(loc)
  acc_query = pcli.accounts.get(acc)

  print(i.name,"",loc_query.name,acc_query.name)  
