ACCOUNT = "5d67c3f06f006f00012b83d1"

users = pcli.users.list_all(q={"account" : ACCOUNT,})

for user in users:

    if user.name[:3] == "PUP":
        print(user.roles)
        pcli.users.update(user,{
            "groups": [
                    "5fc1115c9fa0292bf60e589f",
                    "63491830d6511e89b5741004"
                ],
        })