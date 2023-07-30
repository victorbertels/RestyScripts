UBer = ["624a9426e572ff89f1f29189",
"624a9426e572ff89f1f291b4",
"624a9426e572ff89f1f291fa",
"624a9426e572ff89f1f291e6",
"624a9426e572ff89f1f29196",
"624a9426e572ff89f1f291f0",
"624a9426e572ff89f1f291c8",
"624a9426e572ff89f1f291be",
"624a9426e572ff89f1f291a0",
"624a9426e572ff89f1f291aa",
"624a9426e572ff89f1f291d2",
"624a9426e572ff89f1f291dc",]

account = "5d67c3f06f006f00012b83d1"

rename = pcli.channelLinks.list_all(q={"account" : account , "_id" : {"$in" : UBer}})



for name in rename:
    if name.name[-5:] != "- NEW":
        new_name = name.name + " - NEW"
        print(new_name)
        pcli.channelLinks.update(name,{
            "name" : new_name
        })