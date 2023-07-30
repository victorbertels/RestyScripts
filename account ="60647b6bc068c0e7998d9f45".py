account ="60647b6bc068c0e7998d9f45"
brands = pcli.locations.list_all(q={"account" : account,})

locationIdReferenceMap={"60c3454717b4207e7cc3c4ec" : "6opekSSenMAg2KR8",
 "60c3454717b4207e7cc3c4ed" : "6opekSSenMHe2KRj",
 "60c3454717b4207e7cc3c4ee" : "6opekSSeprXi2PRD",
 "60c3454717b4207e7cc3c4ef" : "6opekSSeprcm2PRI",
 "60c3454717b4207e7cc3c4f0" : "6opekSSeprhv2PRN",
 "60c3454717b4207e7cc3c4f1" : "6opekSSeprmY2PRq",
 "60c3454717b4207e7cc3c4f2" : "6opekSSeprrB2PSC",
 "60c3454717b4207e7cc3c4f3" : "6opekSSeprvx2PT4",
 "60c3454717b4207e7cc3c4f4" : "6opekSSeps0z2PTb",
 "60c3454717b4207e7cc3c4f5" : "6opekSSeps5i2PTg",
 "60c3454717b4207e7cc3c4f6" : "6opekSSepsA42PTl",
 "60c3454717b4207e7cc3c4f7" : "6opekSSepsEh2PTq",
 "60c3454717b4207e7cc3c4f8" : "6opekSSepsJF2PTv",
 "60c3454717b4207e7cc3c4f9" : "6opekSSepsO22PU0",
 "60c3454717b4207e7cc3c4fa" : "6opekSSepsSt2PU5",
 "60c3454717b4207e7cc3c4fb" : "6opekSSepsXZ2PUF",
 "60c3454717b4207e7cc3c4fc" : "6opekSSepsc72PUK",
 "60c3454717b4207e7cc3c4fd" : "6opekSSepsgg2PUP",
 "60c3454717b4207e7cc3c4fe" : "6opekSSepslJ2PUU",
 "60c3454717b4207e7cc3c4ff" : "6opekSSepsps2PUZ",
 "60c3454717b4207e7cc3c500" : "6opekSSepsuf2PVE",
 "60c3454717b4207e7cc3c501" : "6opekSSepszC2PVw",
 "60c3454717b4207e7cc3c502" : "6opekSSept3v2PWi",
 "60c3454717b4207e7cc3c503" : "6opekSSeptAG2PXU",
 "60c3454717b4207e7cc3c504" : "6opekSSeptFF2PY3",
 "60c3454717b4207e7cc3c505" : "6opekSSeptKJ2PYP",
 "60c3454717b4207e7cc3c506" : "6opekSSeptPF2PZH",
 "60c3454717b4207e7cc3c507" : "6opekSSeptTt2PZn",
 "60c3454717b4207e7cc3c508" : "6opekSSepu622PcZ",
 "60c3454717b4207e7cc3c509" : "6opekSSepuAW2Pcu",
 "60c3454717b4207e7cc3c50a" : "6opekSSepuFH2PdC",
 "60c3454717b4207e7cc3c50b" : "6opekSSepuJw2PdH",
 "60c3454717b4207e7cc3c50c" : "6opekSSepuOQ2PdM",
 "60c3454717b4207e7cc3c50d" : "6opekSSepuT92PdR",
 "60c3454717b4207e7cc3c50e" : "6opekSSepuXo2PdZ",
 "60c3454717b4207e7cc3c50f" : "6opekSSepucP2Pds",
 "60c3454717b4207e7cc3c510" : "6opekSSepuhC2Pdx",
 "60c3454717b4207e7cc3c511" : "6opekSSepulo2Pe2",
 "60c3454717b4207e7cc3c512" : "6opekSSepuqf2Pe7",
 "60c3454717b4207e7cc3c513" : "6opekSSepuvP2Pep",
 "60c3454717b4207e7cc3c514" : "6opekSSepuzy2PfM",
 "60c3454717b4207e7cc3c515" : "6opekSSepv4Q2PfR",
 "60c3454717b4207e7cc3c516" : "6opekSSepv8z2PfW",
 "60c3454717b4207e7cc3c517" : "6opekSSepvDb2Pfb",
 "60c3454717b4207e7cc3c518" : "6opekSSepvI22Pfg",
 "60c3454717b4207e7cc3c519" : "6opekSSepvMh2Pfl",
 "60c3454717b4207e7cc3c51a" : "6opekSSepvR82Pfq",
 "60c3454717b4207e7cc3c51b" : "6opekSSepvVU2Pfv",
 "60c3454717b4207e7cc3c51c" : "6opekSSepvaB2Pg0",
 "60c3454717b4207e7cc3c51d" : "6opekSSepvev2PgA",
 "60c3454717b4207e7cc3c51e" : "6opekSSepvjU2PgZ",
 "60c3454717b4207e7cc3c51f" : "6opekSSepvoH2Pih",
 "60c3454717b4207e7cc3c520" : "6opekSSepvtA2Pju",
 "60c3454717b4207e7cc3c521" : "6opekSSepvxt2Pjz"
}




for brand in brands:
  location = brand.get('_id')
  print(location)
  #print(brand.name,",",brand._id)
  print(str(locationIdReferenceMap.get(location,"something")))
  pcli.locations.update(brand,{
    "subscriptions": [
    {
      "brandId": "60647b6bc068c0e7998d9f44",
      "subscriptionId": str(locationIdReferenceMap.get(location,"something"))
    }]
  })