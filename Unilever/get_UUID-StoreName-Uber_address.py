import requests
import csv
unilever = pcli.channelLinks.list_all(q={"account" : "5d67c3f06f006f00012b83d1","channel" : 7})

while True:
    with open(f'/Users/victorbertels/Desktop/Unilever/UnileverData.csv', mode ='w+', newline='') as f:
        header = ['Name','UUID','Address','City', 'PostalCode', 'Country', 'State']
        # header = ['voornaam']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        # writer.writerow({'voornaam':"some bullshit"})


    for link in unilever:
            get_uuid = link.APIKey
            get_location_name = pcli.locations.get(link.location).name


            url = f"https://api.uber.com/v1/eats/stores/{get_uuid}"
            payload={}
            headers = {
            'Authorization': 'Bearer IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAAKCHFvLnFJZP5LzWS9GBWo8AAAAIUfQC7UHRgcFJVgrF8o1pwzbYdLfNGhFfKzXShbhfmz-TDVFdWIvUuKk2nVuSe9TxOa3s5jG_EHLk2yEDAAAAC7HfCM22gPkwPC3ayQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            # try:
            jsonrespsone = response.json()
            name = jsonrespsone.get("name")
            location_address = jsonrespsone.get("location")["address"]
            city = jsonrespsone.get("location")["city"]
            postalcode = jsonrespsone.get("location")["postal_code"]
            country = jsonrespsone.get("location")["country"]
            state = jsonrespsone.get("location")["state"] 
            # print(name,"+-" ,get_location_name ,"-+",get_uuid ,"--++",location_address,"*/" ,city , "=/",postalcode,"*/=" ,"!" ,country ,"#" ,state)
            writer.writerow({"Name" : get_location_name ,'UUID' : get_uuid ,"Address" : location_address , "City" : city , "PostalCode" : postalcode , "Country" : country , "State" : state})
            break



                # print(name)
                # for item in jsonrespsone:
                #     name = item["name"]
                #     print(name)



            # except:
            #     print("no uid found, skip this one")
            #     break


