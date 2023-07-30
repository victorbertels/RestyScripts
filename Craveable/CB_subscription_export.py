#CB subscription export


oporto = '5e7bbf7265013b00010cb6aa'
Red_rooster = "5fe17b1effe9e99933f9f58a"

both = ["5e7bbf7265013b00010cb6aa","5fe17b1effe9e99933f9f58a"]
615e8f1f4875a94524fa9947
query = pcli.locations.list_all(q={'account' : Red_rooster})


for subs in query:
    sub_info = subs.subscriptions
    print(subs.name,"x",sub_info)

