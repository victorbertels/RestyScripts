import requests

url = ["https://630c507964ffb8c1f3b8bb7b-630c50b9eb768833ce2da49c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2be6.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a72.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-631dc62871c3a68d02022e86.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b8c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a66.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b6e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2c2e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b80.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b56.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b86.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ac0.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b02.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2aae.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a84.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630ea91a69bcd44f1f566847.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2af6.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ad2.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a5a.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b1a.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b2c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b98.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a7e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ade.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2aa8.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bda.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2baa.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b50.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2aba.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b74.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bce.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b0e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b5c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ab4.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bc8.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bec.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a6c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2be0.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bbc.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bb6.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bb0.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b9e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2c0a.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b3e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2c34.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bd4.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a90.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bf2.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b62.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ad8.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a7e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bfe.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ae4.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b38.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a8a.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b0e.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2afc.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a96.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2c04.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b26.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bc2.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ac6.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2aa2.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2af0.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b7a.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a60.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2ba4.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2aea.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a9c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b4a.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2a78.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2bf8.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b68.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2acc.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b92.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b20.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630eaa649a14616b9c9d2b44.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",
"https://630c507964ffb8c1f3b8bb7b-630c50b9eb768833ce2da49c.tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl",]



for ur in url:
    try:
        url = ur
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(url)

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.status_code)
        
    except:
        print(ur , "broken")



NotWorking = ["630eaa649a14616b9c9d2b8c",
"630eaa649a14616b9c9d2aae",
"630eaa649a14616b9c9d2bb0",
"630eaa649a14616b9c9d2b62",
"630eaa649a14616b9c9d2ae4",
"630eaa649a14616b9c9d2a8a",
"630eaa649a14616b9c9d2a96",
"630eaa649a14616b9c9d2aea",
"630eaa649a14616b9c9d2b20",
"630ea91a69bcd44f1f566847",
"630eaa649a14616b9c9d2a5a",
"630eaa649a14616b9c9d2baa",
"630eaa649a14616b9c9d2b74",
"630eaa649a14616b9c9d2ab4",
"630eaa649a14616b9c9d2b9e",
"630eaa649a14616b9c9d2bf2",
"630eaa649a14616b9c9d2afc",
"630eaa649a14616b9c9d2ac6",
"630eaa649a14616b9c9d2b44",]


query = pcli.locations.list_all(q={"_id" : {"$in" : NotWorking}})



for i in query:
    print(i.name)