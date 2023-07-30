
query = pcli.locations.list_all(q={'posSystemId' : 10120})


for i in query:
  channelLinks = i.channelLinks  
  print(channelLinks)
  orderhook = i.posSettings.generic.ordersWebhookURL
  synctableURL = i.posSettings.generic.syncTablesURL
  syncFloor = i.posSettings.generic.syncFloorsURL
  syncProdFloor = i.posSettings.generic.syncProductsURL
  print(i.name , "account Name:" , i.account)
  print("orderHook" , orderhook)
  print("synctable" , synctableURL)
  print("syncFloor" , syncFloor)
  print("syncProdFloor" , syncProdFloor)



OrderMateChannels=['6146cc7b8bab71624ef63e7c',
'615ada68c1e4dff97f42d969',
'61779f9350ea25182e16820e',
'61e92848dcdfa812ddb5e33a',
'61e928dd4d4d17d668f54a83',
'61ee0c0444fc487ce2c4ac87',
'61fcfb97a850ebfdcd006d24',
'62007844f37a008b3077ee54',
'620199ec85cc6698f51ac99f',
'62019a91e32ad2dec91c5608',
'62019b178a8d5b8e55fbc62e',
'620af4b2255bd2d71c895bea',
'620af4dc921cd361e5cb8840',
'620b8cedc80bd74e4bf56c37',
'620b8d64c71c5d071db3896c',
'620b8e0727b6b4c62db55279',
'620b8e1bc80bd74e4bf61b31',
'620c783e426ca3ecdcadf706',
'620c787c426ca3ecdcadfc41',
'620c78a8f12beaf8c25b8d2f',
'620d06d552d23ead2c647490',
'620d07395fe527e31fb0def2',
'620d078ef12beaf8c2aa10c6',
'620d08845b8f19255740a8de',
'620e26b05231af3641fd3efd',
'620f26395cabef5080fd0a57',
'6212e5c48f79ed6ed308d281',
'62133c606c43b676df34faf0',
'62133c806c43b676df3511a0',
'62142afd9e59040f119c9501',
'6216f3d8d1c0b3b205902137',
'6216f54cc9745d5027bf027d',
'62172ff1c9745d5027df95f3',
'621db19cb3c20c3609de33e2',
'621dfc27f010b0800d6e9fbe',
'6226b2b294802d9e23e08ae9',
'622a97151ed2227a9c4a996c',
'622a9b4aacffc2cec93cda8d',
'622a9ca72574898e857427bc',
'622a9def1ed2227a9c4be71a',
'6231561bff6fcfae4bfe850b',
'623968ef3ad2cf3fa6163286',
'62401fb0afc0f6d4f8ceb6e9',
'6240321a4aec8eefc9cb9a8b',
'624032240ff04ff57615cf84',
'62403230afc0f6d4f8e37f81',
'6240323e4aec8eefc9cbd20e',
'6242542329fb3083de620c6c',
'6243ce0a8b23f04eabd6aded',
'6243ce1dc5862464fdc0bd5c',
'6243ce2f8feb276b1e6caf97',
'6243ce38c5862464fdc0c20f',
'6243f0358feb276b1e841752',
'624644239b0513271dc158b8',
'62464436f5fccd7366daca3c',
'624647965e591a1b53237e22',
'624665031fc7d5e0e77aa0c0',
'624a406b55d1d7522530c8b4',
'624a54fe649b6f900c71cbba',
'624a5525649b6f900c71d95a',
'624a554de572ff89f1c4a232',
'624a556fe572ff89f1c4b2e7',
'624a557a55d1d752253bb39d',
'624a55f7df5e3ae4a8547707',
'624a7e43df5e3ae4a86d22f0',
'624bbdbca1c46ebf6fb76d4e',
'624bbddfbe122f6683d02cd5',
'624bbde8faf74a98cda2e08a',
'624bbdf6faf74a98cda2f61e',
'624bbe004000050172986ae3',
'624bc69840000501729bdafb',
'624bc6c5d8c185de53996f42',
'624bc6d2d66c6a60b4ac674f',
'624bc726faf74a98cdb17828',
'624bf03ca1c46ebf6fd1e9ee',
'624d0b3f54181050eb30da98',
'624e1e5c1f1026d4c00defb7',
'624e3c2295a0e57118c6f247',
'624e48011f1026d4c0248b90',
'624e4a8a915d8d18c5417ec1',
'624fbf2c343e28c9bb85d980',
'62500167da4f1d439309c02a',
'625001e16bcd374e265d91d5',
'6250023d6bcd374e265dee0b',
'625116ffc1fc0bdd23f954e3',
'6251170b7e3052bfe70865c3',
'62511713c1fc0bdd23f95a4e',
'6251171f63a41c436fbd9dad',
'62511728bb7d45e7643384c1',
'625384a3e2978bc439e4f638',
'6253b858bb7d45e7640ee99d',
'6253ba7cc1fc0bdd23dcee27',
'6253ba9abb7d45e764117b5e',
'6253bac5c1fc0bdd23dd0d9c',
'6253d594e2978bc43926578c',
'6253d5d463a41c436fbba921',
'6253d6c9e2978bc4392740b4',
'6255038d61fd9b9574e81e60',
'62555d9c1937a584d0f6674c',
'625617130ce3042384ae83d0']


CLq = pcli.channelLinks.list_all(q={'_id' : {"$in" : OrderMateChannels}})



for i in CLq:
  orderhook = i.posSettings.generic.ordersWebhookURL
  synctableURL = i.posSettings.generic.syncTablesURL
  syncFloor = i.posSettings.generic.syncFloorsURL
  syncProdFloor = i.posSettings.generic.syncProductsURL
  print(i.name , "account Name:" , i.account , "CL ID " , i._id)
  print("orderHook" , orderhook)
  print("synctable" , synctableURL)
  print("syncFloor" , syncFloor)
  print("syncProdFloor" , syncProdFloor)
