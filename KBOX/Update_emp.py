from enum import unique


query = pcli.users.list_all(q={"account" : "62fc44dc934376949a733248" , })



for i in query:
    roles = i.roles
    groups = i.groups
    is_unique = groups.count("5df8e2ca7de0b70001e0dfeb")
    if is_unique == 0:
        groups.append("5df8e2ca7de0b70001e0dfeb")
        pcli.users.update(i,{
            "groups" : groups

        })





   