tags = pcli.channelLinks.list_all(q={'account' : '6007cc878320c413b235d0f8'})


for tag in tags:
    channel = tag.get('channel')
    print(channel)
    if channel == 1:
        pcli.channelLinks.update(tag , {
            "tags": [ "Deliverect"
            ]
        })
    elif channel == 14:
        pcli.channelLinks.update(tag , {
            "tags": [ "Zomato"
            ]
        })
    elif channel == 20:
        pcli.channelLinks.update(tag , {
            "tags": [ "Talabat"
            ]
        })
    elif channel == 2:
        pcli.channelLinks.update(tag , {
            "tags": [ "Deliveroo"
            ]
        })


tags = scli.channelLinks.list_all(q={'account' : '5ecbb60fa6ed980001c439f9'})

### Update Dynamic
tags = scli.channelLinks.list_all(q={'account' : '5ecbb60fa6ed980001c439f9'})

for tag in tags:
    channel = tag.get('channel')
    taglist = tag.get('tags')
    print('taglist',taglist)
    print(channel)
    if channel == 1:
        taglist  += ['Deliverect']
        print('new' ,taglist)
        scli.channelLinks.update(tag , {
            "tags":  taglist
         })
    elif channel == 7:
        taglist  += ['Uber']
        scli.channelLinks.update(tag , {
            "tags":  taglist
         })
    elif channel == 16:
        taglist  += ['Wolt']
        scli.channelLinks.update(tag , {
            "tags": taglist
         })
    elif channel == 2:
        taglist  += ['Deliveroo']
        scli.channelLinks.update(tag , {
            "tags": taglist
         })



