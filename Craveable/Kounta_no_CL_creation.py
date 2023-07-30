role = "5d7a638e6e5f4900016d3123"

users = pcli.users.list_all(q={"account" : "5e7b70272bb18e000197dedb"})


for user in users:
        roles = user.groups
        if role in roles:
            print(roles)

            roles.remove(role)
            print(roles)
            print("-----------------------------------------------------------------------------")



            pcli.users.update(user,{"groups" : roles
        })

