

query = pcli.accounts.list_all(q={"posSystem": 10086,    "region": "AUS",
})



for i in query:
  print(i.name,'*', i._id)
  users= pcli.users.get(i._id)

accounts =['60daf210f755c8aa671ca112',
'60f1607e857fdbecd63580ff',
'6107d0dd9ff63189a676b3dc',
'612385158f8432d9e149948e',
'616417307c5c62326d8b69ed',
'616d46156efadb675e1230e2',
'6188d8d13bfa814a2590aa9a',
'618b65554f295ad6931c3714',
'618be886339e6d6f39797a70',
'61acc089bbde8daf66118ef4',
'61acc4884cca9a67dd6e99fb',
'61bfced4f0b7890abfb14c91',
'61e5e3c9e94c0434990b5639',
'61f8a71ef21e437048bc64d5',]

users = pcli.users.list_all(q={'account':{"$in":accounts}})


for i in users:
  accountID = i.account
  getacc = pcli.accounts.get(accountID)
  print(i.name,'**',i.email,'--',getacc.name)



query = pcli.accounts.list_all(q={"posSystem": 25})

