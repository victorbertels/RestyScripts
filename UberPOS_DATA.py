### Check All KBOX UBER STATUS 
import requests
import time
import json
from datetime import datetime


token = "IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAAdRaSwz6Bg25-hD6FvkSok8AAAAIZwh_t7W1bryODmkakCcbVBP_iz7gs78YIymRsQFEozRqPle0wg7vagU6Uqp-ZgESTZSsIJhkliuD-E5DAAAAL4WSUzo58qfcreOeyQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU"

acc_ids=["62fc44dc934376949a733248"]
query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':7})


uuidList = []

for i in query:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")   
    uuid = i.channelSettings.storeId
    uuidList.append(uuid)
    # location = i.location
    # loc_name = pcli.locations.get(location)
    # print(
    #     "Channel link with id :" ,i._id ,"and name: ",i.name," on location" , loc_name.name," has UUID:",uuid 
    # )

for uuid in uuidList:
    url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"

    payload={}
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    if response.ok:
        jsonResponse = response.json()
        pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
        integration = "Enabled" if jsonResponse.get("integration_enabled") else "Disabled"
        order_manager = jsonResponse.get("order_manager_client_id")
        print(f"{dt_string}, {uuid}  , posIntegration  = {pos_integration} , integration = {integration} , orderManager = {order_manager}")
        time.sleep(10)    
    else:
        print(response.text,"for UUID: ",uuid)
    


### ACTIVATE ALL UBER's
import requests
import time
import json

token = "IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAAdRaSwz6Bg25-hD6FvkSok8AAAAIZwh_t7W1bryODmkakCcbVBP_iz7gs78YIymRsQFEozRqPle0wg7vagU6Uqp-ZgESTZSsIJhkliuD-E5DAAAAL4WSUzo58qfcreOeyQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU"

acc_ids=["62fc44dc934376949a733248"]
query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':7})


clId = []
deliverectToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjQxNzg5ODcsImV4cCI6MTY2NDI2NTM4NywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.MQ8Tpccg_JFp0gcTw3RQeO9I9HXmt8DSE1Old3lgcUDrsK03P4B_HFAvgu6PKrCk4AK_9Nt6zJ74Pr0L-nu8EkgsREaxTK53WAqmyLq-EB2AvLqa5Yocn2MDIhQOnfQ4rZkeUV-Lb0rWC0sn5xB0H8hZeWNeJvqDtp2Mkt5edWnvG6jnYmLscxopXW2Cm_V0KAZ_KNkjXUNj-6Glkx4Px57vuW2q47Qo2XsfTGGVsN3v5E4qcCXvlZRzbAbfG7VraRZCO4yX-kIkcUumikb2bBOZPBU5pbIWqpiaFHIoOtEpONzq1pTMphy_pCI_rgSWECK031DjX1iMLK9gCkdXyA"
for i in query:

    uuid = i.channelSettings.storeId
    clId.append(i._id)
    # location = i.location
    # loc_name = pcli.locations.get(location)
    # print(
    #     "Channel link with id :" ,i._id ,"and name: ",i.name," on location" , loc_name.name," has UUID:",uuid 
    # )

for clink in clId:
    firstUrl = f"https://api.deliverect.com/disableChannelLink/{clink}"
    secondUrl = f"https://api.deliverect.com/activateChannelLink/{clink}"

    payload = {}
    headers = {
    'Authorization': f'Bearer {deliverectToken}'
    }
    first_response = requests.request("POST", firstUrl, headers=headers, data=payload)
    time.sleep(2)
    second_response = requests.request("POST", secondUrl, headers=headers, data=payload)
    print(clink , first_response)
    print(clink , second_response)
    
    # if response.ok:
    #     jsonResponse = response.json()
    #     pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
    #     integration = "Enabled" if jsonResponse.get("integration_enabled") else "Disabled"
    #     order_manager = jsonResponse.get("order_manager_client_id")
    #     print(f"{uuid}  , posIntegration  = {pos_integration} , integration = {integration} , orderManager = {order_manager}")
    #     time.sleep(3)    
    # else:
    #     print(response.text,"for UUID: ",uuid)
    

