# import requests



#     base_url = "https://api.deliverect.com/locations?where={"
#     subscription = "subscriptions.subscriptionId"
#     url = f"{base_url}{subscription}{sub}}"
#     print(url)

import requests
import urllib.parse


# subs = ["169k6gTIk9L85C0BX"]
# for sub in subs:
# # Create the URL with the f-string
#     base_url = "https://api.deliverect.com/locations"
#     subid = "subscriptions.subscriptionId"
#     openBracket = "{"
#     closeBracket = "}"
#     url = f"{base_url}?where={openBracket}{subid} : {sub}{closeBracket}"

#     # Use the requests library to perform URL encoding
#     encoded_url = requests.utils.quote(url)

#     print(encoded_url)



subs = ["169k6gTIk9bRrC1tN",
"169k6gTIk9YhLC1hn",
"169k6gTIk9YntC1io",
"169k6gTIk9YdYC1hg",
"169k6gTIk9ZJiC1m0",
"169k6gTIk9TffC17q",
"AzZR1PTIpaoEZA091",
"AzZRDVSmB1J7g1Bne",
"16CKbbSnoJy953vL3",
"6111fb1c433c61c26941fbd3",
"6111cdf65389ff89bb274c68",
"16CKaxSv9O8wjCyqv",
"16CKaxSv9OESrCyuP",
"AzZR5tSwSJy6qGdXV",
"16CKOOSuxrzaj1Fi3",
"6opesSx3ecxS4Cwf",
"AzZR8CT3itsqp24Bm",
"16CKVzT3iv7woxFM",
"16CKX8T4NBZSi8NZr",
"16CKUrT7OUXec1ne4",
"AzZRCeT6psnyb5Tpl",
"16CKUrT7OUWEO1nca",
"16CKT8TAEBuMK4Nhi",
"16CKT8TAEBuEP4Nhb",
"AzZR6ATClv34A1pjV",
"AzZR7RTBYoYZzVnY",
"16CKQsTE7q2Ir1lYp",
"169k6qTFEKVE714COS",
"169k6qTFEKSGP14CAU",
"169k6qTFEKSkO14CCU",
"16CKT4TI4P9inKeS",
"AzZRDSTLpjV0wNAsf",
"AzZR1qTKhP4SG2wVe",
"AzZR1qTKhP5Yz2wZM",
"AzZR1BTLNFbzRgNEE",
"169k7fSJtZ2q93Jln",
"16CKOgSNqkEDW1uD2",
"169k6iSHLBB6S1GEf",
"AzZR6YSObOPWc1ky9",
"16CKW0STEL2jj2esl",
"AzZRAqSfyMHzbcnPi",
"AzZR5NSiOrAqSFo6l",
"AzZR0nSeYHum45SK0",
"AzZR3nSjjAj9h1xvM",
"AzZR9dSgLFH8D86R",
"AzZR3mSkNmAodopaF",
"AzZR7LShfl8M52tRE",
"16BcrgS8gHto0yYU",
"16BcjhS8yZR8X1kXF",
"AzZRBYSiUlhBIzGM",
"16BZFPS8yYr0p1li4",
"AzZwBpSAHtfr32D19",
"AzZw66SFI1qZQGJi",
"AzZR9BSFrAr5x2KPx",
"AzZRDhSGiSNd74xyi",
"16CGamSFMoyVG1rRJ",
"AzZRDhSGiSNiK4xyt",
"AzZRDhSGiSTJa4y7q",
"16CKVpSykcL3T9NG9",
"AzZR3nSjjAjQL1xwk",
"AzZRDhSGiSNVW4xyT",
"16CKQfSov22LYCFmy",
"16CKXmSUl7cL7749A",
"16CKb4SLDAM9a1Uf7",
"16CKPZSI8FffnBMgb",
"169lIFS8yXM0v1m9E",
"169k6gTIk9b7FC1rv",
"169k6gTIk9ZOAC1mF",
"AzZR0TSiJ4SpGfpx",
"16CKQsTE7q07P1lSZ",
"AzZR60T0PjjH9GSix",
"16CKW0STEKvua2ehb",
"16CKNhSgdmzwX5Oys",
"AzZw8GS9KyR6FA3k8",
"AzZR4GSbc29JgwVBN",
"16CKT4TI4P9vzKeg",
"16CKQsTE7q25f1lXP",
"169k6gTIk9UnpC1Cy",
"AzZRAaSRu56pO57P1",
"16CGdRS9dHQdHrdU",
"AzZR7qT91bq0G3iBt",]


all_Kounta_locations = pcli.locations.list_all(q={"subscriptions.subscriptionId": {"$in" : subs}})


# https://api.deliverect.com/locations?where={"subscriptions.subscriptionId": "169k6gTIk9bRrC1tN"}&projection={"account":1}

count = 1
for loc in all_Kounta_locations:
    location = loc._id
    account = loc.account
    get_email = pcli.users.list_all(q={"account" : account})
    for user in get_email:
        print(loc._id)
        print(loc.name)
        print(user.email)
        print(user.name)
        print("-----------")
        print("-----------")
        print("-----------")
    for sub in loc.get("subscriptions",{}):
        print(sub.get("subscriptionId",{}))
        sub_id = sub.get("subscriptionId",{})
        if sub_id in subs:
            count += 1
            update_location_to_suspended = pcli.locations.update(loc._id , {
                  "status": "SUBSCRIBED",


            })
            channelLinks = loc.get("channelLinks" ,{})
            for channelLink in channelLinks:
                pcli.channelLinks.update(channelLink,{
                    "status": 3
                })

            # print(channelLinks)            
            # print(loc._id)
            # print(sub_id)
            # print(count)



# for sub in subs:
#     print(sub)
#     get_location_be_subscription = pcli.locations.list_all(q={ "posSystemId": 25, ""})

































# url = "https://api.deliverect.com/locations?where={%22subscriptions.subscriptionId%22:%20%22%22}&projection={%22account%22:1}"
# print(url)
# payload = {}
# headers = {
#   'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODU0ODkyMzIsImV4cCI6MTY4NTU3NTYzMiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.EtCl3of8-w5jOkewfBeRpQ05D1H1Pbeo794hmJ45Ki567amGWk4YhtjzJcVagfEJcBuOzU965zzD6e9Pdcee4UhXMTIOIPY2JGYSdSMJ8V96MNBvL4jsY30DeLXFv8oUb-IZ_G5KNBsp8VsUA2OXYz9jYxalqvHOA14o_5xgh43y4_U6JunSc2xqQLf8uSPr26bXVMRKIw0Ch2VjQe-Ws7V5nbs-xPCM0W7RZCX0Xq1Kt5I7HWbstrxlQoRThcuAmwi7az-tB9AtxTwbd35ZIOpJMgdGylkW4M-bfUYYWad1VKzF2dEm0uvAZfpT8ynBARz_Tf4kINgyr8tZjwhrnA'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
