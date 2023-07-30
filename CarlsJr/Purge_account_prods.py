loc = "6268ce08e97401166b98cd19"

query = pcli.products.list_all(q={"account": "633d14f8ea170601672a3ff5"})

for prod in query:
    pcli.products.delete(prod)



