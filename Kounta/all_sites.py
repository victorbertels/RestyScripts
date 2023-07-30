possystem = 25

kounta = pcli.accounts.list_all(q={"posSystem" : possystem})

for acc in kounta:
    location = acc.get("locations" , {})
    for loc in location:
        print(loc)
        get_location = pcli.locations.get(loc)
        for site in get_location:
            print(site)
            siteId = site.posSettings.get("kounta").get('site',{})
            print(siteId)