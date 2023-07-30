CTP=["P-CH-gvF0-2",
"P-BA-micb-2",
"P-CL-UtxL-1",
"P-SR-Z6y9-2",
"P-TE-XUnW-1",
"P-TE-dwJd-1",
"P-BA-P7GY-1",
"P-BA-HgC3-1",
"P-SR-yJH9-1",
"P-TE-Wwe2-4",
]

CTPM =["618d2f5cd542d39de0571bf3",
"6195c9dfdcd44c9618fab909",
"6195d6bc0ed724c234bd9539",
"61963d8d03b9e525d0552d8e",
"61963e30354ace90ca059f59",
"61964a6094bdbcf226ab8df0",
"61964aeba3e89cd47475c7df",
"61964b4a38ef284b8b3fca92",
"61964ba8bbbce279117c3360",
"61964bfa03b9e525d05e49c0",]

env=pcli


query = env.products.list_all(q={"account" : "615e8f1f4875a94524fa9947","plu" : {"$in":CTP}})
secon_query = env.products.list_all(q={"account" : "615e8f1f4875a94524fa9947" ,"_id" : {"$in":CTPM}})

for i in query:
  subproduct =i.subProducts[0]
  print(subproduct)

for prod in query:
    pcli.products.update(prod,{
          'isVariant' : True
      })
 
for mod in secon_query:
  pcli.products.update(mod,{
          'isVariantGroup' : True

  })

