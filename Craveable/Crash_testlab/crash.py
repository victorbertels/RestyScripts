import requests
import threading

def do_request():
    while True:
            
        url = "https://5fe17b1effe9e99933f9f58a-5ff385cac6cc4ade72524c1a.tunnel.deliverect.com/EGateway/SimphonyPosApiWeb.asmx"

        payload = "<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/wsdl/soap/\">\n    <soap:Body>\n        <GetConfigurationInfo xmlns:ns0=\"http://micros-hosting.com/EGateway/\">\n            <employeeObjectNum>91043</employeeObjectNum>\n            <configurationInfoType>\n                <int>1</int>\n            </configurationInfoType>\n            <revenueCenter>12</revenueCenter>\n        </GetConfigurationInfo>\n    </soap:Body>\n</soap:Envelope>"
        headers = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'http://micros-hosting.com/EGateway/GetConfigurationInfo'
        }

        response = requests.request("POST", url, headers=headers, data=payload).text

        print(response)
threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()

print(threads)


