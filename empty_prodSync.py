acc = "62b46ee18007f811ef5080f1"
loc = "62b46f145b739a3c494efc71"
env = pcli

body = {
   "accountId":acc, 
   "locationId":loc,
   "products" : [
      {
         "plu":"victor",
         "name":"bertels",
         "price":0
      }
   ],
   "categories":[
      {
         "name": "Australia",
         "posCategoryId": "SATE"
      }
   ]
}
resp = env.call("/productAndCategories","POST",json=body)
print(resp)