## Curb NEW all combo's to MEAL DEALS. isInternal : False -> isCombo:True


internal_quer = {'account' : "6037d4911d6ed071c4f321f4",  "isInternal": True}
internal_prods = pcli.products.list_all(q=internal_quer)


query = {'account' : "6037d4911d6ed071c4f321f4" , "plu" :{"$in" : ["DEAL-SOULBOWL-P-LE-mb1m-22",
"DEAL-SMASH-P-SM-1Uof-34",
"DEAL-SMASH-P-BA-orMa-35",
"DEAL-SMASH-P-BE-CRlt-36",
"DEAL-SMASH-P-KI-FNQu-37",
"DEAL-SMASH-P-SM-WE3Q-38",
"DEAL-ELBURROP-ME-gUvC-7",
"DEAL-ELBURRO-P-FL-F8IQ-8",
"DEAL-ELBURRO-P-ME-t4WR-9",
"DEAL-ELBURRO-P-FL-OyqF-10",
"DEAL-BAHGAWK-P-BA-YTfM-5",
"DEAL-BAHGAWK-P-TH-b6bB-145",
"DEAL-BAHGAWK-P-TH-AgUa-147",
"DEAL-BAHGAWK-P-TH-zjvH-2",
"DEAL-CANDIE-P-CA-xmRs-186",
"DEAL-MACKA-P-MA-TCP7-258",
"DEAL-MACKA-P-WI-aInj-259",
"DEAL-ITALIANSIN-P-TE-JvIP-281",
"DEAL-ITALIANSIN-P-TA-13uA-283",
"DEAL-ITALIANSIN-P-TA-QlZt-290",
"DEAL-WOKYOU-P-WO-6Xtg-294",
"SMOOTHIES-CURB-P-HO-vCDX-3",
"SLUSH-CURB-P-SL-zTxD-326",
"MILKSHAKES-CURB-P-MI-zoJo-327",
"JARRITOS-CURB-B-JA-Ino1-9",
"DIPS-CURB-P-DI-TTXu-11",
"MAIN-CURB-P-CA-mMSr-158",
"MAIN-CURB-P-OU-TdZx-341",
"MAIN-CURB-P-WA-losT-1",
"MAIN-CURB-P-SM-FE3h-1",
"MAIN-CURB-P-SM-qrNK-2",
"MAIN-CURB-P-BU-YOX3-352",
"MAIN-CURB-P-BO-zyFg-9",
"MAIN-CURB-P-CH-uRMK-354",
"MAIN-CURB-P-BU-8L6L-355",
"MAIN-CURB-P-KO-sPJi-359",
"MAIN-CURB-P-WH-pKSO-363",
"MAIN-CURB-P-RE-Vk5O-364",
"MAIN-CURB-P-OU-arFy-367",
"SIDE-ALL-P-TH-1a7r-2",
"TORTILLACHIPS-CURB-P-TO-Rld5-334",
"DRINKS-CURB-P-SO-wvpJ-330",
"DRINK-ALL-P-JU-upgm-324",]}}

prods = pcli.products.list_all(q=query)

for prod in prods:
  print(prod.name)
  pcli.products.update(prod,{
        "isCombo": True
  })
  

query = {'account' : "6037d4911d6ed071c4f321f4"}
links = pcli.channelLinks.list_all(q=query)

for link in links:
    pcli.channelLinks.update(link,{
          "posSettings": {
            "generic": {
                "logOps": True,
          }}})



#set meal deals to isInternal : True 

internal_quer = {'account' : "6037d4911d6ed071c4f321f4",   "isCombo": True}
internal_prods = pcli.products.list_all(q=internal_quer)


for prod in internal_prods:
      internal = prod.get("isInternal")
      print(internal)
      if internal == False:
            pcli.products.update(prod,{'isInternal' : True})