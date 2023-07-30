cp = pcli.channelProducts.list_all(q={'account' : "5fe17b1effe9e99933f9f58a" , 'menu' :'6229337b8b7452f13f81b4c3',"imageUrl":{'$exists' : True}})

cp =pcli.channelProducts.list_all(q={'account' : "5e7bbf7265013b00010cb6aa" , 'menu' :'6237b426f0a33fd1d52060f3',"imageUrl":{'$exists' : True}})

print(cp)

menu=["5ffe35a136d307eb88019d46",
"602b07854d0eb07b5f19e503",
"6086e1b0a00154d2b145f977",
"608ff4254509c73e0c8b83d2",
"60932a2c67dad5de595d8f95",
"60a13882a0d15e73e7d1f6bd",
"60ab46edfa66ac8d7c264820",
"60ac5c40fa66ac8d7c8d1fcf",
"60ac5f7a69f7c29bdbb646a4",
"60bcd9b9f14f0eab67aebb58",
"60bcda016319b36fc68b4ef2",
"60c2c0bf17b4207e7c8b9cc3",
"60d30be8134631d0ab984f15",
"60d9c6c8dd61f1ba41339dc8",
"61552a790996750033e43766",
"615fca9f759f9c673b3a896c",
"617a9a26245c5c9e4d7b2229",
"61945b2ec035ba4a9c5e1ce5",
"61f2245f31271cb178b7eaef",
"61f735f7f21e437048d8827b",
"61f9b897a861d435fac40d77",
"61f9bc7b17bc9aca59a66f1f",
"6229337b8b7452f13f81b4c3",
"62314884e817a0016d7b0bd1",
"62314ccb8c66e0b6b99d8368",
"6233ba151550b1dca746a296",
]


cp = pcli.channelProducts.list_all(q={'account' : "5fe17b1effe9e99933f9f58a"  ,"imageUrl":{'$exists' : True}})

for c in cp:
    del c.imageUrl
    pcli.channelProducts.replace(c, c)