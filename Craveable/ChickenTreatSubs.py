locationrefmapChicken = {

}


CT ={'account' : '615e8f1f4875a94524fa9947'}
CTlocs = pcli.locations.list_all(q=CT)

for subs in CTlocs:
    subss = subs.subscriptions
    print(subss)
    location = subs.get('_id')
    print(subs._id,str(locationrefmapChicken.get(location,"not live yet")))
    pcli.locations.update(subs,{
        "subscriptions": [
        {
      "brandId": "601865b3917dda2a713c1edb",
      "subscriptionId":str(locationrefmapChicken.get(location,"TO BE ADDED"))
    }
  ]})





RR_query ={'account' : '5fe17b1effe9e99933f9f58a'}

RRlocs = pcli.locations.list_all(q=RR_query)

for subs in RRlocs:
    subss = subs.subscriptions
    print(subss)
    location = subs.get('_id')
    print(subs._id,str(locationIdReferenceMap_RR.get(location,"Not live yet")))
    pcli.locations.update(subs,{
        "subscriptions": [
        {
      "brandId": "601865b3917dda2a713c1edb",
      "subscriptionId": str(locationIdReferenceMap_RR.get(location,"TO BE ADDED"))
    }
  ]})


