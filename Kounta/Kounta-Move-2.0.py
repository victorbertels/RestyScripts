'''
ran those 
v1menuacc = pcli.accounts.list_all(q={"posSystem": 25, "deliverectVersion": ""})
mbmenuacc = pcli.accounts.list_all(q={"posSystem": 25, "deliverectVersion": "2.0-menubuilder"})
psmenuacc = pcli.accounts.list_all(q={"posSystem": 25, "deliverectVersion": "2.0-productsync"})
V2menuacc = pcli.accounts.list_all(q={"posSystem": 25}), "deliverectVersion": "2.0"})
'''

'''give me this list of Acc_id's'''

acc_ids= ["5f175e2b2ead84471a72072f",
"5f5a43e64e695362a11ae0ec",
"5efe67eede63fd0155c82ce7",
"5f073e0cb5f7d7974c23a9a2",
"5f31ba4bbfd9917b8f84b957",
"5f329c6fda4d7405cf9f0880",
"5f3c4ce1319f989249bc5b0f",
"5f3c697c08306bccf930de10",
"5f3c699f08306bccf930de2c",
"5f3ffa4e8f239013598c7b7b",
"5f3ffc2cb9a2dcbfeec7814d",
"5f401c45b9a2dcbfeeca461e",
"5f440f646d21bb255d5bb520",
"5f44111c6d21bb255d5c8559",
"5f4411936d21bb255d5c8eb9",
"5f45c68fc1ffc75a76d5b9ac",
"5f4912e14c90f7ec7b2d4885",
"5f4ca821c249410801784677",
"5f4d08d347277ebd98228553",
"5f4d19f747277ebd9824eab9",
"5f4e0b1d6ca7dbc69f50fd27",
"5f4fb242b86920ed9b902cad",
"5f51a3f462fcfa91c7a00354",
"5f52264062fcfa91c7c0e0a0",
"5f562c0f881308ff0a180872",
"5f5652ebd909a53bc5b7422f",
"5f580669afbd08f6463efef2",
"5f5806abafbd08f6463f56a5",
"5f580713afbd08f6463f56e4",
"5f58fbda4b38e801855ffaf8",
"5f5a41f94e695362a11aabdb",
"5f5e8d2d8882d7bfbb371fef",
"5f5fed479e26dca61f6bfbdc",
"5f607f0d9e26dca61f722463",
"5f6284770b1a1c7bf166e44f",
"5f6772dc8564b770390e4793",
"5f68adfc8564b770392f2d38",
"5f6af5e81a99f79003ffc6bd",
"5f6afcac1a99f7900300a92b",
"5f6b712009e27ea72049ee87",
"5f6ce0c983d1e220307e1075",
"5f6da25e83d1e220308a2650",
"5f732e973e853bd15e3d0768",
"5f734d54afde9bb5a2228a35",
"5f7358fe3e853bd15e44d270",
"5f7db080dc365bd0a306ec28",
"5f85815411c5d664c9766c62",
"5f88542c3a69161a09a4d605",
"5f8df6c2529d2df6da851bdd",
"5f8ee40e662bdd01401fcbbf",
"5f8f152cde80234f2302683f",
"5f915f922359ca4c7a9d996d",
"5f91932c3151e20ff727c959",
"5f92b3863151e20ff769448e",
"5fa30a072df16dcd43387ac1",
"5fa4076c50f6ac7edbe491d9",
"5fad4ad782f3d2194ea6d475",
"5fad72b434efc992affdd45a",
"5fb7b2a8fb032ac07dd7971b",
"5fbfa58aea0f52ea3c9abb43",]


# update to Deliverect 2.0 version

query = pcli.accounts.list_all(q={'_id':{'$in':acc_ids}})

for i in query:
    pcli.accounts.update(i,{
        "deliverectVersion": "2.0",
    })