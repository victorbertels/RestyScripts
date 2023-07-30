
acc = pcli.accounts.get("6305b450a373ba8b4a6c4566", only={'POSAccessProfiles',"name"})

for a in acc:
    pcli.accounts.update("6305b450a373ba8b4a6c4566",{
        "POSAccessProfiles" : []
    })
    
    
    print(a)
print(acc)


import toDict


import datetime
acc = pcli.accounts.list_all(q={"posSystem": 48}, only={'POSAccessProfiles',"name"})
my_list=[]
currentTime = datetime.datetime.now()
x = currentTime.strftime("%Y-%m-%d")
for a in acc:
    try:
        if a.POSAccessProfiles != []:
            
            accountID = a.get("_id")
            accountName = a.name
            first_dict = a.POSAccessProfiles[0]
            expires_at = first_dict["expiresAt"]
            client_id = first_dict["clientId"]
            environment = first_dict["servicesUrl"]
            dict = {"account" : accountID , "name" : accountName , "renewal date" : expires_at}
            my_list.append(dict)
            # print(f"{acc_name} with id {accountID}, will expire at {expires_at}")
            print("---------------------------")
            print("Generated on: ",x)
            print("Account Name: ",a.name)
            print("Acc ID: ",accountID)
            print("Client ID: ",client_id)
            print("Environment: ",environment[:13])
            print("Expires At: ",expires_at)
    except:
        continue




sorted_list = sorted(my_list, key=lambda x: x['renewal date'])



Posacc = pcli.accounts.list_all(q={"_id" : {"$in" :accids }}, only='POSAccessProfiles')
for pac in Posacc:

print(acc)

for a in acc:
    print(a)
    print(ac._id)
    print(ac.POSAccessProfiles)
print(acc)




acc = pcli.accounts.get("63435e96e54f9c12e91c9745", only='POSAccessProfiles')
print(acc)



acc = pcli.accounts.get("61bcb26d68ddb52a44aceb3d")
pcli.accounts.update(acc, {"POSAccessProfiles": [{"name" : "_SimphonyProfile", "token" : "eyJraWQiOiI1MTQxZjM0OS0zMDdjLTRhNTgtYTVmOC0xZDlkMjJmZjZmZDciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI5NmVjMDQxOC1hYTE3LTQyN2ItYjQ3My1hZjNkZjA1NzJkNTciLCJhdWQiOiJVVWhRTGpObU1ESmtPVEppTFdFM05HVXROREk0TXkwNFl6Z3dMV1UwTURjeFptVTJZemcxWXc9PSIsImlzcyI6Imh0dHBzOlwvXC93d3cub3JhY2xlLmNvbVwvaW5kdXN0cmllc1wvaG9zcGl0YWxpdHlcL2Zvb2QtYmV2ZXJhZ2UiLCJleHAiOjE2NjQ4ODAwNTUsImlhdCI6MTY2MzY3MDQ1NSwidGVuYW50IjoiYmZlNTY1YjItYmJiNS00YTY2LTk5NmMtNTQ0YmVhMGQyOGFlIn0.OUhbyQdFi-89Ku3UdZGHeFEdf8xRIcND3SZiCb_n7UkoUKTg88iA2FKb06_ttYl96R1UeTqaqGlPpvzGlDYyLe39ctOKOg1uOzu1kzt8F5fIr-r9rk_y5fAtnzZYl34KX07cKi-WX96ayoEoocOd9nUygO-ZjuZSTXg80jTBGCpm6l-AZdGrN_sAHkh0D29LlNdBgjVG-3ATqCJGLLMp5_bHSWzwRaFhjnBDjB9to9wlg4GxbcWWAmFo5K1fH6RUk-k77S820JKcxCiBY2cpWavt5hK1ySG_9OhHEduHrUSHHqKn67fr8FCnJVw3VuBT8WZyJtPPkiQTWnc6Sb__yLKAvru_ymjKsUCcUDFlC6UNc8JIY2nrnvAT3fYizd-oqX_67f3QGjUUdud_5SHmfVI1nMiACNZbwZByX4Ea-DFuIHux2GVDOZeaqL9Gr9JuJkMvDv6e02X7FZuYkwzRZSJ7SYhncpXJklzB2Vk74QyQTxXAt8w_bQJ7vfRsTJQf", 
"refreshToken": "UUhQLnRrbGl1bXZsc3NpbXFqYWF4dXVwbHRqcXFjcmN1b2FpYWprZmNlaGxxbHR4bGlreGp2YmhpYWJrdmNuaGJzYWx6YnRkbm9wbnhrbm51b2F1a3hqbWtndWV6bWFiYmRwZXlvemlxZmtobnpqbWJycHRmbGxxanhzZm1teHRtemdu", "expiresAt": "2022-10-03T12:00:01.000000Z", "authUrl": "https://mta4-ohra-idm.oracleindustry.com/oidc-provider/","servicesUrl": "https://mta4-sts.oraclecloud.com/api/v1/", "clientId": "UUhQLjNmMDJkOTJiLWE3NGUtNDI4My04YzgwLWU0MDcxZmU2Yzg1Yw==", "orgName": "qhp"}]})





loc = pcli.locations.list_all(q={'account' : '62253102c34b8f03264bc9ff','ignorePOSOrderStatuses' : True})




menus = pcli.channelMenus.list_all(q={"account" : "63abd7593662ec3abb11db6f"})
for menu in menus:
    print(menu._id)

menus = ["647b8f14475468ee758c2414",
"642dd21e7df0fa970d7040bc",
"6416fb8ac9ea3b1418d1a89b",
"6416fabbe22abbf95ba8f3e2",
"6416f9f0b50398a787dbee95",
"6416f9431df33f9a950937a6",
"63d9f7624ac17d02869bcc15",
"63d9efb1516833322f6c2e9b",
"63d9dbc950f80f4f445aa5f9",
"63d9d91c45fc7b1ca9f739a3",
"63d9d89b76cef200d1c0cec6",
"63d9d82f5dd0970c3e45ea29",]
channelProducts = pcli.channelProducts.list_all(q={"account" : "63abd7593662ec3abb11db6f", "menu" : {"$in" : menus}})

print(channelProducts)