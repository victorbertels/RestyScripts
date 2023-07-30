#PAM NEW TENDER

query ={'account' : '5e81f14758168e0001d981d5',"location":{"$in" : [
    "5f0830509f26c0077d566597",
    "5f6e0d7583d1e22030a522a9",
    "5f6e0f2283d1e22030a568d1",
    "5f96890e5bbe4e3aa1c45b7b",
    "5f2d31fac324cbc85cfff718",
    "5f96890e5bbe4e3aa1c45b79",
    "5fa7ea920e210c3d583c281f",
    "5fb4ef44e9145d3df6c86ee7",
    "5f6e0f7283d1e22030a59912",
    "5fa7ea920e210c3d583c2828"
]}}
env = pcli
links = env.channelLinks.list_all(q=query)
#Channels: 
# 9 = JE 
# 2 = Deliveroo
# 7 = Uber
# 10015 = Order ahead

for link in links:
    env.channelLinks.update(link,{'posSettings.simphony.notPaidPaymentType' : "901"})
    print(link.get('name'),'got adjusted to',link.posSettings.simphony.notPaidPaymentType)


