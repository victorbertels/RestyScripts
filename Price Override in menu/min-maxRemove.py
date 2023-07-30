account = "629856bdb3d5d7f4453ccd9b"
menuId =["62aacf9ee130e84ee9175be5","62c3f1660923942ca0058936","629de604ab47ae42c014e169","629de5f6d22edffe5299f992"]


cp =pcli.channelProducts.list_all(q={'account' : account , 'menu' :{"$in" : menuId}, 'productType' : 3})


for c in cp:
    pcli.channelProducts.update(c,{
        "min" : 0,
        "max" : 0 
    })


for c in cp:
    try:
        print(c.min , "min")
        print(c.max, "max")
        print('--------------')


    except:
        print("noname and no overrides",c.deliverectProductId)
