account  = "630c507964ffb8c1f3b8bb7b"

query = pcli.channelLinks.list_all(q={"account" : account , "ignorePOSOrderStatuses" : {"$exists" : False} })
query2 = pcli.locations.list_all(q={"account" : account, })
query2 = pcli.channelLinks.list_all(q={"account" : account, })


for q in query:
   
    pcli.channelLinks.update(q,{
          "ignorePOSOrderStatuses": True

    })



for q2 in query2:
    if q2.ignorePOSOrderStatuses == False:

        pcli.locations.update(q2,{
            "ignorePOSOrderStatuses": True

    })


for q in query2:
    pcli.channelLinks.update(q,{
          "posSettings": {
    "maitred": {
        "sendDiscount" : False,


    }}})


for ch in query:
    channel = ch.channel
    if channel == 1:
        pcli.channelLinks.update(ch,{

        "posSettings":{
        "maitred":{
            "postPaidPaymentMediaV2":"10",
            "prePaidPaymentMediaV2":"10",

        }}})



    elif channel == 12:
               pcli.channelLinks.update(ch,{

        "posSettings":{
        "maitred":{
            "postPaidPaymentMediaV2":"19",
            "prePaidPaymentMediaV2":"19",

        }}})






    elif channel == 26:
               pcli.channelLinks.update(ch,{

        "posSettings":{
        "maitred":{
            "postPaidPaymentMediaV2":"16",
            "prePaidPaymentMediaV2":"16",

        }}})





    elif channel == 7:
               pcli.channelLinks.update(ch,{

        "posSettings":{
        "maitred":{
            "postPaidPaymentMediaV2":"10",
            "prePaidPaymentMediaV2":"10",

        }}})
