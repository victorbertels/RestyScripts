accs = pcli.accounts.list_all(q={"posSystem": 25})

acc_ids = []

for i in accs:
    accId = i._id
    acc_ids.append(accId)

users_list=[]
users = pcli.users.list_all(q={'groups' :{"$in":["5e5911a017467d0001cb46de"]}})
for i in users:
    userId = i.account
    users_list.append(userId)

Kountas = []
accs = pcli.accounts.list_all(q={"_id": {"$in" : users_list}})
for a in accs:
    posSys = a.posSystem
    if posSys== 25:
        print(a._id)
        Kountas.append(a._id)
Kountas


users = pcli.users.list_all(q={'account' :{"$in":Kountas}})


for user in users:
    if "5e5911a017467d0001cb46de" in user.groups:
        print(user._id)
        old_groups = user.groups
        print("Old Groups: ",old_groups)
        new_groups = old_groups.remove("5e5911a017467d0001cb46de")
        print("mnew Groups: ",new_groups)





accs = pcli.locations.list_all(q={"posSystemId": 25,"posSettings.kounta.site" : {"$exists" : True}})

for i in accs:
    print(
        i.name,"***",i.posSettings.kounta.site
    )