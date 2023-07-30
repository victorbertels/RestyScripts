oporto = "5e7bbf7265013b00010cb6aa"

query = pcli.channelLinks.list_all(q={"account" : oporto})



for i in query:
    print(i.reportingEndpoints)
    pcli.channelLinks.update(i,{
        "reportingEndpoints": [
    {
      "endpointType": 10,
      "endpoint": "https://craveablebrands.au-alerts.freshservice.com/alert_profiles/50000000153/integrations/50000000125/alerts?auth-key=eyJhbGciOiJIUzI1NiJ9.eyJhX2lkIjo2NywiYXBfaWQiOjUwMDAwMDAwMTUzLCJzX2lkIjo1LCJ0cyI6MTYyODc0Mjc3Ny43NDA5MDY3fQ.mwEHIwrTgU6uULx893LtZixuNLL4QxTD-E93m52-wqw",
      "statusTrigger": [
        120
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://craveablebrands.au-alerts.freshservice.com/alert_profiles/50000000153/integrations/50000000125/alerts",
      "statusTrigger": [
        120
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://us-central1-prod-dw-etl-deliverect.cloudfunctions.net/dev-dw-etl-deliverect-webhook",
      "statusTrigger": [
        4
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://us-central1-prod-dw-etl-deliverect.cloudfunctions.net/dev-dw-etl-deliverect-webhook",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 1
    }
  ]

    })
   