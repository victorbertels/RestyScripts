#find kounta where usedefault is false:


kounta = pcli.locations.list_all(q={'posSystemId': 25 , 'posSettings.kounta.useDefaultPLU' : False})
acc_ids =[]


for i in kounta: 
    acc = i.account
    acc_ids.append(acc)
    print(acc_ids)
    loc_name = i.name
    acc_name = pcli.accounts.get(acc)
    print(acc_name.name,"---",loc_name,"***",i._id,"*-*-",acc_name._id)
