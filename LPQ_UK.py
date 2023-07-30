urls = pcli.locations.list_all(q={'account':'6054c1d5c0e70796115e1d3e'})

for ur in urls:
    pcli.locations.update(ur, {
        "posSettings": {
            "generic": {
                "anonymizeCustomer": False,
                "logOps": False,
                "readonly": False,
                "hasDirectTableIntegration": False,
                "bufferOrders": False,
                "syncProductsURL": "",
                "ordersWebhookURL": "https://le-pain.iikoweb.co.uk/api/integrations/delivery-injector/webhook/89a64c35-0f8b-49b5-8c91-dfe044eafb1f",
                "locationId": "",
                "orderItemRemarks": "intactItemRemarks",
                "alwaysSendAllSnoozedProducts": True
    }}},propagate = )
    