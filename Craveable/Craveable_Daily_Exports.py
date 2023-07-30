from socket import TCP_NODELAY
import requests
import json
import time
import datetime
import csv

today = datetime.datetime.now()
print(today)
dt = datetime.datetime.now()- datetime.timedelta(days = 1)
tomorrow =  datetime.datetime.now() + datetime.timedelta(days = 1)
tomorrowDate = tomorrow.date()
print(tomorrowDate)
Yesterday = dt.date()
todayDate = today.date()

print("Paste your Deliverect Token")
token = input()

allAcc = ["5e7bbf7265013b00010cb6aa","5fe17b1effe9e99933f9f58a","615e8f1f4875a94524fa9947"]




    

#create reports
for account in allAcc:        
    url = "https://api.deliverect.com/v1/export/orders"

    payload = json.dumps({
    "format": "csv",
    "accounts": [
        f"{account}"
    ],
    "locations": [],
    "begin": f"{Yesterday}T00:00:00Z",
    "end": f"{Yesterday}T23:59:59Z",
    "fields": [
        "pickupTime",
        "_created",
        "scheduledTime",
        "location",
        "channelOrderDisplayId",
        "channel",
        "status",
        "posReceiptId",
        "orderType",
        "payment",
        "paymentAmount",
        "paymentRebate",
        "note",
        "serviceCharge",
        "deliveryCost",
        "discountTotal",
        "tip",
        "subTotal",
        "tags",
        "channelLink",
        "taxTotal",
        "taxTotalComputed",
        "failureMessage",
        "isTestOrder"
    ],
    "targetAccount": "6005123c4d6a5febf07a2138",
    "splitItemsToSeparateRows": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# fetch Reports


second_url = """https://api.deliverect.com/operationReports?page=1&cursor=716411f70feed9371c9c13d28b8c8840&where={%22account%22:{%22$in%22:[%226005123c4d6a5febf07a2138%22]},%22_created%22:{%22$gt%22:%22"""f"{Yesterday}T13:00:00.000Z%22,%22$lt%22:%22{todayDate}""""T12:59:59.999Z%22}}&sort=-_created&max_results=50"""


payload = ""
headers = {
  'Authorization': f'Bearer {token}'
}

reportID = []
response = requests.request("GET", second_url, headers=headers, data=payload)
jsonresponse = response.json()
# operationReport = jsonresponse.get("_items")[0]
for opReport in jsonresponse.get("_items"):
    if opReport["user"]["name"] == "Victor Bertels":
        reportID.append(opReport["_id"])

with open(f'/Users/victorbertels/Desktop/Craveable/CRAVEABLE-DAILY-EXPORT-{Yesterday}.txt', 'w', newline='') as f:
    header = ['URL']
    writer = csv.DictWriter(f, fieldnames=header)
    for report in reportID:
        csv_url = f"https://api.deliverect.com/v1/export/sign/{report}"

        payload = ""
        headers = {
        'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", csv_url, headers=headers, data=payload)

        csv_report = response.json()["url"]
        print(csv_report)
        writer.writerow({"URL":csv_report})