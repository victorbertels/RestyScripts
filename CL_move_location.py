# CL array on account
query = {'account' : '5e7cb1c565013b000110df09' , '_id':{'$in':["6048f33bdc9167d22110e1a3","6048f525a38405cbd920b1ff","6048f548a38405cbd920b364","6048f4ec5f3170fc1c96d25f","6059e6856bba63d18efed4cf","6059e5c0b0bb975945b99c3d","6059e738d7790d6dc4593e13","6059e7116bba63d18efef2da","6059e6aed7790d6dc458fc90","6065cac11ac801089015e12f","6065ca651ac801089015d38a","6065ca7f36d8a9bdf167f2a7","6065caf3deeb2ae8dbf7c133","6065cad8336b9cfbd6ca1e9f"]}}

# patch CL with new location ID
links = pcli.channelLinks.list_all(q=query)
for link in links:
    pcli.channelLinks.update(link,{'location': '609bd30780511370c9b7217a'})


## NEW array for old and new loc
array_new_loc = ["6065ca7f36d8a9bdf167f2a7",
"6065cad8336b9cfbd6ca1e9f",
"6065ca651ac801089015d38a",
"6065caf3deeb2ae8dbf7c133",
"6065cac11ac801089015e12f",
"6048f33bdc9167d22110e1a3",
"6048f4ec5f3170fc1c96d25f",
"6048f525a38405cbd920b1ff",
"6048f548a38405cbd920b364",
"609bd3094d64e6f174d7e4e9",
"6059e6856bba63d18efed4cf",
"6059e6aed7790d6dc458fc90",
"6059e7116bba63d18efef2da",
"6059e5c0b0bb975945b99c3d",
"6059e738d7790d6dc4593e13",]

array_old_loc = [
    "60489fe046bc25d72c8962f1",
    "6048f2f3a38405cbd91e5155",
    "6048f312dc9167d22110d300",
    "6048f42601093122d02d1759",
    "6048f446a38405cbd91f8724",
    "6048f49f01093122d02d3976",
    "6048f577a38405cbd920b546",
    "6050fd4e05293f3243665cf3",
    "6051176e28519c3b90a2ec75",
    "6059e4e86bba63d18efd8345",
    "6059e55db0bb975945b91348",
    "6059e582d7790d6dc45885b6",
    "6059e7d46bba63d18eff5796",
    "6065ca4536d8a9bdf167ef93",
    "6065cb0a36d8a9bdf1680f99",
    "6065cb20deeb2ae8dbf7d43c",
    "6065cb3636d8a9bdf1681e02",
    "6065cb52deeb2ae8dbf7f9a6",
    "6065cb6cdeeb2ae8dbf816fd"]




# Patch new array of CL id on previous and new location.
new_loc_query = {'account' : '5e7cb1c565013b000110df09' , '_id' :'609bd30780511370c9b7217a' }
old_loc_query = {'account' : '5e7cb1c565013b000110df09' , '_id' :'60489fa8d5fede1639495e7b' }

locs_new = pcli.locations.list_all(q=new_loc_query)
locs_old = pcli.locations.list_all(q=old_loc_query)

for loc in locs_new:
    pcli.locations.update(loc ,{ "channelLinks" : array_new_loc})

for loc in locs_old:
    pcli.locations.update(loc ,{ "channelLinks" : array_old_loc})



poland = pcli.call('/simphony/5f0c3cda9b689fce5c68e281/productinfo/')

