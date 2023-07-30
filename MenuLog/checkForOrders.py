channelLinks = [
    "6480623ac5d4fff99944e157",
"647ec0688e816ce6e3787c22",
"647446dba7affa52588605d7",
"64893c7d0fa6a1a9cd1a2fef",
"6413c90aaadac39a32fc9d2b",
"645b23039e08960f836bf43b",
 "60dafbbfdf9dac5d93ff0e81",
"648923615db81f47631f2b18",
"648bae39521e1369e0134adc",
"648bc74a230d5c28315e7c05",
"648bc59ccc665b131fab3f1c",
"648bc51c987d7fe8862448d4",
"648bc4e07abed0c708def142",
"648bc4997f87ad16452b7675",
"648bb2380ef7400c0ec3d18c",
"648bb14ecbe88c8153f6f62a",
"648bb068be9203a53bb4bc2b",
"648baf84c23b16dac6cb4b10",
"6413c90aaadac39a32fc9d2b",
"648a7b7d1e4f53f7ec30556d",
"648bb390ff7b2b6d3e517701",
"6476a5767f43c1f9e11857e2",
"6457609f54f1a8010c795e3e",
"64708af15a68f5ad8b705374",
"647cb840c49b9ab6b8f576f8",
"64805836ffebe23bc89aa742",
"648c45993163ddf063beed6c",
"6411509a30fd7a0adbdd5a19",
"646c2aae75b29c226ebfd4ca",
"644b274802632bfad8636ba6",
"64917f0191c92b79c987391c",
"64924c9d5571f6f4ad0d62d3",
"6477873111e24cae7e27afdd",
"647d23ea0665b0548967a0ce",
"6487d054fab6c6b9b18dc7e1",
"64914f17948c25f22e6f5a2b",
"649152c832bfc974e0a7e166",]



query = pcli.channelLinks.list_all(q={"_id" : {"$in" : channelLinks}})
for q in query:
    account = q.account
    id = q._id
    get_orders = pcli.orders.count(q={"account" : account, "channelLink" : id ,"_created":{"$gt":"2023-06-01T14:00:00.000Z","$lt":"2023-06-23T13:59:59.999Z"}})
    if get_orders:
        print(id , get_orders)



