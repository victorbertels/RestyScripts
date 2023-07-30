import requests
import json
import time
import datetime
import csv


dt = datetime.datetime.now()- datetime.timedelta(days = 30)
Yesterday = dt.date()
print("Paste your Deliverect Token")
token = input()

allAcc = ["61f16a85c10f898fd52ab03c"]
 

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
    "targetAccount": "62b00ab0c843643ddb6f1aca",
    "splitItemsToSeparateRows": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


#fetch Reports


second_url = "https://api.deliverect.com/operationReports?page=1&cursor=2f967d058c5bfa90cb47a7cec390770b&where={%22account%22:{%22$in%22:[%2262b00ab0c843643ddb6f1aca%22]},%22_created%22:{%22$gt%22:%222022-10-25T13:00:00.000Z%22,%22$lt%22:%222022-10-26T12:59:59.999Z%22}}&sort=-_created&max_results=50"

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
        urls = []
        urls.append(response.json()["url"])
        print(urls)
        for url in urls:
            response = requests.get(url)
            open("exportsss22.csv", "wb").write(response.content)


#         print(csv_report)
#         writer.writerow({"URL":csv_report})





# URL = "https://storage.googleapis.com/deliverect-exports-production/5cbec927c6489f0001d11867/orders-6358a553030fe245d8705e00.csv?Expires=1666755682&GoogleAccessId=deliverect-exports-gcs%40deliverect-production.iam.gserviceaccount.com&Signature=YoHtlBu3vl7HZEAg7uYsTdMWLDU7ytr2gkZsfn3rBbya64LDKK5SJKnFCLZlbFCwVXB6mqjNxfLAJeNHIqY4RcQbtCFDumiNEOTNSMsLKW2BlTN7GT4PpnUHlWT0NfLVPRph9QBRy8qia86fm2wUVsELOnams3lf5C%2BPexmjPNY%2FGm0%2BBa%2BcEUFe4ZHzvdQ24Br8Qrk76GlSQKJpKZbztHJkKUDS5pQQcfIOeFF24VRKVjK4t3jvEOxEVxf09wRSW%2FbYdD6L9rcRonSuqiRVqEOqH14dApOpTmhCYHHd%2F3iBRFUX5vp7CoGRKzE1rGIbnh1oMyjDlaM9W7NkyVbE6w%3D%3D"
# response = requests.get(URL)
# open("exports.csv", "wb").write(response.content)