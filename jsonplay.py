import json
order = {
    "header": {
        "orgShortName": "s13",
        "locRef": "1008",
        "rvcRef": 1,
        "checkRef": "a14f1a1d2cd84da7bb4a263140e38ff200004243",
        "idempotencyId": "ace89bae-c6b8-47b6-a957-a51b15acd2bd",
        "checkNumber": 910,
        "checkName": "",
        "checkEmployeeRef": 999999998,
        "orderTypeRef": 26,
        "tableName": "0",
        "tableGroupNumber": 0,
        "openTime": "2022-07-26T01:04:02.3589234Z",
        "guestCount": 0,
        "language": "en-US",
        "isTrainingCheck": False,
        "informationLines": [
            "Delivery by resto",
            "ASAP (15:26)",
            "Address: 4 The",
            "Krook, 8888KL, Gent",
            "Notes: This is a",
            "test order",
            "DELIVERECT #T169763"
        ],
        "status": "closed",
        "preparationStatus": "Uninitialized"
    },
    "menuItems": [
        {
            "menuItemId": 3002006,
            "definitionSequence": 2,
            "name": "Whole Chicken",
            "quantity": 1,
            "unitPrice": 18.9900,
            "priceSequence": 1,
            "total": 18.9900,
            "seat": 0,
            "surcharge": 0,
            "condiments": []
        }
    ],
    "comboMeals": [
        {
            "comboMealId": 3903999,
            "seat": 0,
            "comboItem": {
                "menuItemId": 3903999,
                "definitionSequence": 1,
                "name": "Deliverect Test Burger Combo",
                "quantity": 1,
                "unitPrice": 99.9900,
                "priceSequence": 2,
                "total": 99.9900,
                "seat": 0,
                "surcharge": 0,
                "condiments": []
            },
            "mainItem": {
                "menuItemId": 3003999,
                "definitionSequence": 1,
                "name": "Deliverect Test Burger",
                "quantity": 1,
                "unitPrice": 0,
                "priceSequence": 1,
                "total": 0,
                "seat": 0,
                "surcharge": 0,
                "condiments": [
                    {
                        "condimentId": 3999903,
                        "definitionSequence": 1,
                        "name": "Bacon - Streaky",
                        "quantity": 1,
                        "unitPrice": 0,
                        "priceSequence": 8,
                        "total": 0,
                        "seat": 0,
                        "surcharge": 0
                    },
                    {
                        "condimentId": 3999999,
                        "definitionSequence": 1,
                        "name": "Deliverect Test Condiment",
                        "quantity": 1,
                        "unitPrice": 0,
                        "priceSequence": 5,
                        "total": 0,
                        "seat": 0,
                        "surcharge": 0
                    },
                    {
                        "condimentId": 3999999,
                        "definitionSequence": 1,
                        "name": "Deliverect Test Condiment",
                        "quantity": 1,
                        "unitPrice": 0,
                        "priceSequence": 7,
                        "total": 0,
                        "seat": 0,
                        "surcharge": 0
                    },
                    {
                        "condimentId": 3999999,
                        "definitionSequence": 1,
                        "name": "Deliverect Test Condiment",
                        "quantity": 1,
                        "unitPrice": 0,
                        "priceSequence": 8,
                        "total": 0,
                        "seat": 0,
                        "surcharge": 0
                    }
                ]
            },
            "sideItems": [
                {
                    "menuItemId": 3006001,
                    "definitionSequence": 1,
                    "name": "Regular Chips",
                    "quantity": 1,
                    "unitPrice": 0,
                    "priceSequence": 1,
                    "total": 0,
                    "seat": 0,
                    "surcharge": 0,
                    "condiments": []
                },
                {
                    "menuItemId": 4003003,
                    "definitionSequence": 1,
                    "name": "Coke No Sugar 390ml",
                    "quantity": 1,
                    "unitPrice": 0,
                    "priceSequence": 1,
                    "total": 0,
                    "seat": 0,
                    "surcharge": 0,
                    "condiments": []
                }
            ]
        }
    ],
    "extensions": [],
    "taxes": [
        {
            "taxRateId": 1,
            "name": "10% GST",
            "total": 10.82
        }
    ],
    "tenders": [
        {
            "tenderId": 602,
            "name": "MenuLog",
            "total": 120.03,
            "chargedTipTotal": 0
        },
        {
            "tenderId": 101,
            "name": "Cash",
            "total": -1.0500,
            "chargedTipTotal": 0
        }
    ],
    "totals": {
        "subtotal": 118.9800,
        "subtotalDiscountTotal": 0,
        "autoServiceChargeTotal": 0,
        "serviceChargeTotal": 0,
        "taxTotal": 0,
        "paymentTotal": 118.9800,
        "totalDue": 0.0000
    }
}


# print(order)
jsonData = json.loads(order)

header = jsonData.get["header"]
print(header)