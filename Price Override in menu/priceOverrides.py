# give me the account and menu ID
account = "62044dee1ce54b2bb3b8502f"
menuId = "6254d8f62db26405b05a1198"

# get all the products from the menu
channelProducts =['62044f7db0a5c25581cc4690', '62044f7db0a5c25581cc4692', '62044f7db0a5c25581cc46f3', '62044f7db0a5c25581cc46d5', '62044f7db0a5c25581cc46d7', '62044f7db0a5c25581cc46f5', '62044f7db0a5c25581cc4678', '6236d5d2afa8bc87598a4fbe', '62044f7db0a5c25581cc46d9', '620cc9a8c55ace749c840a14', '62044f7db0a5c25581cc46e7', '62044f7db0a5c25581cc4676', '62044f7db0a5c25581cc467e', '62044f7db0a5c25581cc467a', '62044f7db0a5c25581cc467c', '62044f7db0a5c25581cc46e5', '62044f7db0a5c25581cc46ed', '62044f7db0a5c25581cc46eb', '62044f7db0a5c25581cc46e9', '6204a0036624910820942f5d', '62044f7db0a5c25581cc46e3', '62044f7db0a5c25581cc466e', '62044f7db0a5c25581cc4670', '62044f7db0a5c25581cc464c', '62044f7db0a5c25581cc464e', '62044f7db0a5c25581cc465c', '62044f7db0a5c25581cc464a', '62044f7db0a5c25581cc4668', '62044f7db0a5c25581cc466c', '62044f7db0a5c25581cc4654', '62044f7db0a5c25581cc4656', '62044f7db0a5c25581cc4648', '62044f7db0a5c25581cc4664', '62044f7db0a5c25581cc4662', '62044f7db0a5c25581cc4660', '62044f7db0a5c25581cc465e', '62044f7db0a5c25581cc466a', '62044f7db0a5c25581cc46a0', '62044f7db0a5c25581cc46ac', '6204a314481330fdec22bf29', '620cc9a8c55ace749c840a0b', '62044f7db0a5c25581cc469a', '62044f7db0a5c25581cc469e', '62044f7db0a5c25581cc469c', '6204a0036624910820942f5c', '620cc9a8c55ace749c840a1d', '6204a314481330fdec22bf07', '62044f7db0a5c25581cc46ae']

priceproducts = pcli.products.list_all(q={"_id" :{'$in' : channelProducts}})


for i in priceproducts:
    oldPrice = i.price
    newPrice = round(oldPrice * 1.15)
    print(newPrice)
    pcli.products.update(i,{
        "price" : newPrice
    })



#channelCategories =['62044f7db0a5c25581cc4690', '62044f7db0a5c25581cc4692', '62044f7db0a5c25581cc46f3', '62044f7db0a5c25581cc46d5', '62044f7db0a5c25581cc46d7', '62044f7db0a5c25581cc46f5', '62044f7db0a5c25581cc4678', '6236d5d2afa8bc87598a4fbe', '62044f7db0a5c25581cc46d9', '620cc9a8c55ace749c840a14', '62044f7db0a5c25581cc46e7', '62044f7db0a5c25581cc4676', '62044f7db0a5c25581cc467e', '62044f7db0a5c25581cc467a', '62044f7db0a5c25581cc467c', '62044f7db0a5c25581cc46e5', '62044f7db0a5c25581cc46ed', '62044f7db0a5c25581cc46eb', '62044f7db0a5c25581cc46e9', '6204a0036624910820942f5d', '62044f7db0a5c25581cc46e3', '62044f7db0a5c25581cc466e', '62044f7db0a5c25581cc4670', '62044f7db0a5c25581cc464c', '62044f7db0a5c25581cc464e', '62044f7db0a5c25581cc465c', '62044f7db0a5c25581cc464a', '62044f7db0a5c25581cc4668', '62044f7db0a5c25581cc466c', '62044f7db0a5c25581cc4654', '62044f7db0a5c25581cc4656', '62044f7db0a5c25581cc4648', '62044f7db0a5c25581cc4664', '62044f7db0a5c25581cc4662', '62044f7db0a5c25581cc4660', '62044f7db0a5c25581cc465e', '62044f7db0a5c25581cc466a', '62044f7db0a5c25581cc46a0', '62044f7db0a5c25581cc46ac', '6204a314481330fdec22bf29', '620cc9a8c55ace749c840a0b', '62044f7db0a5c25581cc469a', '62044f7db0a5c25581cc469e', '62044f7db0a5c25581cc469c', '6204a0036624910820942f5c', '620cc9a8c55ace749c840a1d', '6204a314481330fdec22bf07', '62044f7db0a5c25581cc46ae']


# get all the channel Categories and save its products in that list

menu = pcli.channelProducts.list_all(q={"menu" : "62d8dedc4f5f40a8cab11fe1"})

for i in menu:
    try:
        print(i.price,"old i")
        del i.price
        print(i,"new i ")
    except:
        print("no price betch")


        
        pcli.channelProducts.replace(i, i)
print(channelProducts)


targetProducts = pcli.channelProducts.list_all(q={
    'deliverectProductId' :{'$in' :channelProducts, "menu" : "6254d8f62db26405b05a1198"}
})



targetProducts = pcli.channelProducts.list_all(q={ "menu" : "6254d8f62db26405b05a1198"})


channelMenuProducts = pcli.channelProducts.list_all(q={
    'plu' :"XD4IDTEQBDFXBW3WHSGXV5N3", }
})





cp =pcli.channelProducts.list_all(q={'account' : account , 'menu' :menuId,"price":{'$exists' : True}})


for c in cp:
    del c.price
    pcli.channelProducts.replace(c, c)
    