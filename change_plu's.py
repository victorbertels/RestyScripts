from random import randint
plussss=["Fried_flipped",
"Choice_of_Add_Ons",
"Choice_of_Add_ons",
"Fried_Flipped",
"2_Scoops",
"2_Scoops",]
query = {'account' : "6123587eb44397bec9b80594",  'plu':{"$in":plussss}}
products = pcli.products.list_all(q=query)

for prod in products: 
  #print(prod.plu)
  plus = prod.get("plu")
  print(plus)
  if plus[0] == "#":

    new_number =randint(100000,9999999)
    new_plu = str(new_number) + plus
    print(new_plu)
    #pcli.products.update(prod , {"plu" : new_plu})
    print('i was', plus,'and now i am  because', new_plu , 'is my new plu')
  else:
    print("do nothing")



