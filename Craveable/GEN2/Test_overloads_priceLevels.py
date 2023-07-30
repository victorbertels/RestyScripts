account = "63290d3fdceae416df65c7e8"

query = pcli.products.list_all(q={"account" : account , "location" : "636055a2cb9fccb436a3e76c" , "overloads" : {"$exists" : True}})


for i in query:
    print(i.plu ,"----",i.overloads)