import requests
import time

importTable = {
"6332b9438db91358ec268526" : "xPEpUqEeUmAyzd51opo8uESV",
"6332b943efbaf5fe1031619c" : "s7KMhXswfVume7cwaiFfirrQ",
"6332b94488318d0df3de6712" : "NGDY5743BU1D5FEPK8YjbkiW",
"6332b944c0b6239ce8c23de1" : "BhD1hoUXouebvkGFc3552fQo",
"6332b94550c4d639c1529d85" : "n3uZdFKHDSu8khYHq1Z71ice",
"6332b9457136995018c004c8" : "PkpRf7JQVFJwynY6tnNdumDf",
"6332b946efbaf5fe1031634b" : "4tTWUWBgdjfMRcQC2Ahzg7Jv",
"6332b947df516710d8e63ced" : "BeBmjLAhx6h5tL8zWQTnGhSJ",
"6332b9d68db91358ec26d66c" : "1xhmCgyKfj9NJGGVMACA7BMV",
"6332b9d3c0b6239ce8c2b3b2" : "Lcwar7Yrkdsv5JadLwzyKJhZ",
"6332b9d6c0b6239ce8c2b3fd" : "ppC7QzWPVbycuZ5Yk4KyVibP",
"6332b9d750c4d639c152f7c4" : "V4jFPbQeJkbZqXmQzYtqKJ9j",
"6332b9d7efbaf5fe1031982d" : "WNFpraYFtzZSrgDSPvU8ogVQ",
"6332b9418db91358ec2683b4" : "6mLWn8XtEQRNhfFhTXwQyZq9",
"6332b9417136995018c0025e" : "yzcUXxYXxqTTEJujDHPbqmX7",
"6332b9af044575e99117c326" : "eTBPFuqYyj5ii73TFyAhRTz3",
"6332b9b150c4d639c152ee1f" : "qy59th8caGTKheFYnNYdosEM",
"6332b9aeefbaf5fe103186fa" : "vXjjcvDCcUZqZYw9SG8iPytx",
"6332b9b0a67a59472963aff9" : "so86xsG5yz3kVNGLu1vBCuVn",
"6332b9387136995018bfffe9" : "sYNrweArZ3Ez2GyDf3YALsQj",
"6332ba5aefbaf5fe1031e61c" : "dyTdJwUZm4ZcL2wER6eHfMJM",
"6332ba5b50c4d639c15347af" : "VRrSeG6736Y6yB2Cx4EMjRVG",
"6332ba5cefbaf5fe1031e757" : "mBib3orWTMGDF6qSKu2mazNw",
"6332ba5b59dd9071a46b0330" : "JUrLy94vHceZL7QmRBh1t4ja",
"6332ba5a5905bf37c3e75139" : "teZoX4KYoofntRa6NbEM7Rg1",
"6332b9a5efbaf5fe10318493" : "h5Xb5Pyvqx2ga5yyzA1bVDso",
"6332b9a28db91358ec26a630" : "qK1hfgyYjWMgPQQQu6Hgu6vo",
"6332b9a350c4d639c152ebe5" : "KxA8fsFdAVURbfWFocn7fW2Q",
"6332b9a65905bf37c3e71ab2" : "QewuhCU8qb5pQpo3m1oYZBq3",
"6332b9a7df516710d8e67a03" : "cxTi7fdY78P6HVZHwyhE5KBU",
"6332b9365905bf37c3e6d1c6" : "DuLZ6ipmsH6k3zwfYFuvSfkC",
"6332b937df516710d8e63834" : "fHzgN999rkxRyhFe2euaem8F",
"6332b9387136995018bfffe9" : "uSfC2LXng24Tin4NsWZGJrNA",
"6332b9ac044575e99117c279" : "HtecxnC3DoymqPY8J8tsStdV",
"6332b9aaefbaf5fe10318541" : "3B9g2JNuQWUZhFsHYUzjc812",
"6332b9aba3da85cd965fbe52" : "gqskYddLpYznBkrtb1dLcpPk",
"6332b9ac59dd9071a46a3704" : "A38bsvSXzaxLsbHdBbDf16bL",
"6332b932a3da85cd965ee623" : "duiYUGiGJ2Q7UWe2YqrUkWWG",
"6332b931c0b6239ce8c23bc5" : "9KFXnDiM16WxUiizF2wbggFW",
"6332b93188318d0df3de26a1" : "4dX4WUXDq5niAvV9K6zpqeF9",
"6332ba53a3da85cd966034ee" : "zseuJZA5r2sgLpFwoR4e3iiE",
"6332ba54e27ec8b08cead1c8" : "XHvrWAwXYkhAQzz9ZxfqWX6D",
"6332ba567136995018c079fa" : "rnexzL8EUTKKyzhbkgZWuNxJ",
"633bacbf2ef3c14e805dde8a" : "jYFzui1wTNKsHXesLrEYTYwQ",
"6332ba52c0b6239ce8c2da20" : "8eA9C4hfj6fDuxj6nMvi2b1r",
"6332ba5359dd9071a46b0101" : "Mvn1CLzM7Nf28fDg5rquArJC",
"6332ba517136995018c079b1" : "U66w86kK7cvdA4XkpWjijotH",
"6332ba4f5905bf37c3e74df2" : "LtmHQWtJhZSKP5xra2RPDAm6",
"6332ba517136995018c07986" : "aTX9y8xH4DLK1BX5zZVqiX9N",
"6332ba50a3da85cd966027c7" : "GQhG5fFa5toHg1CpBfkDG4Hj",
"6332ba5250c4d639c1533922" : "cFZATCjEvfa5QAp1Bh5Hg78U",
"633bacf6a71ce73bf02b6e2b" : "KxftdfhR8aGFDf8jHqo1uMc5",
"6332b9f471568ff258eb76a2" : "o7udusRRgUAxCEjruF5rBRgw",
"6332b92d59dd9071a469f13d" : "r3HLwnTwtfdhMYAu171cReyf",
"6332b92befbaf5fe103136ea" : "GaxqcPqPW1n6tGpnY7NQuK9b",
"6332b92befbaf5fe10313707" : "Dq7uBBKUJD2tHr4iCEcYqG4V",
"6332b92d59dd9071a469f13d" : "8Q3Rokp2bNyuQsMAK6NL6HSd",
"6332b92c71568ff258eb135f" : "v1311gG5beEmroivoNbLztB9",
"6332ba485905bf37c3e74d3f" : "Scazv3vLmwRTGymvQmhcGXP1",
"6332ba4edf516710d8e708df" : "c1fvzi18dYuLU4pBPmAx9Wqv",
"6332ba4850c4d639c15328f4" : "m3CpbjfPytnuve2ZH1FCok7Z",
"6332ba4c044575e991182f15" : "1fmyrcyLgS1B7mtMuMmncREQ",
"6332b92950c4d639c1529846" : "odw8MEqHFQpfbeqehNfmf1ab",
"6332b92888318d0df3de1cef" : "8ohQ9xtyj5X2GJVjt7MfqVCT",
"6332b927df516710d8e622a6" : "b5b1siBJV9F3mNEgQmmcqmWV",
"6332b9a1e27ec8b08cea4ce5" : "N2epWsJsVgnTJBNc8XpcNTyc",
"6332b99e044575e99117beb6" : "p2sKyDKo6FjtXavBVmZvTEtA",
"6332b99fc0b6239ce8c285d9" : "3jX9yHVB9VtDjLiaCDjCEYzC",
"6332b9a0e27ec8b08cea4c0a" : "xCxzSRDj18ABGqESV8EbjBmR",
"6332b923a67a5947296382b7" : "FHwo1RJtsGygx1NbaCDsE7yX",
"6332b92250c4d639c152973f" : "x8zMutVuY2ER2pMP9nVd6UJi",
"6332b9217136995018bfe1cf" : "DGcxBvd1ewbjBusDn3a4YGgA",
"6332b9d35905bf37c3e72d28" : "3gdWwRz8NK2JGZHJFGHQ3cFP",
"6332b9cee27ec8b08cea5fe5" : "PmQip3ZMHPFZAbnDoiKcuevp",
"6332b91b7136995018bfe0fc" : "HGU7SzhXLjXLgse91Ai3WGQV",
"6332b91a59dd9071a469caa8" : "q3hbYp1Ebo1nzbK9Vn6jWvfx",
"6332b91cc0b6239ce8c23615" : "hwLW2o8LETzp1iNidQECwNEs",
"6332b91a59dd9071a469ca55" : "caGbYgJayRFBzipEbsfoNW7n",
"6332b9178db91358ec267100" : "hW63aXqpc3MbZ5tWhSHcPJZi",
"6332ba46df516710d8e707bb" : "m5z9bjU6ptkMXjd8QDxpBGip",
"6332ba4550c4d639c1532806" : "NMt1NJRkSrNeAU5R6hwqVsS6",
"6332ba4750c4d639c153288d" : "SmjnrUxDXzqzz4ZwctgphQ7t",
"6332ba44044575e991182def" : "9XNoEEqWfBH3HAU25cxCa4Sn",
"6332ba4471568ff258eb9024" : "akNuVKiYkczDM43N5DEbiFPs",
"6332ba43efbaf5fe1031cdc2" : "VseNSQ1sKYhu3nBfxo1WK8gD",
"6332b9935905bf37c3e70315" : "42rykXHeYtQSHLgewt77ZPLN",
"6332b997efbaf5fe1031821a" : "S3xyva7gtjb5Jwvjkn6WriMw",
"6332b99588318d0df3de88ce" : "u2DHLuYW8J9txzYzNUpditVk",
"6332b996df516710d8e67637" : "MEJVTD97eEyYrBvtiUw6nUbu",
"6332b99388318d0df3de87e9" : "iNEBWE2AGbHJLeArxVPBES3g",
"6332b9985905bf37c3e70375" : "AYQNDkiUtAL2n4jAtv5HkseG",
"6332b994c0b6239ce8c282d1" : "M3kkpY7NaZrMkkoHCLrcj23k",
"633bad2b2e6ae555f9ed20e3" : "pac3mKbxXcLsmzxmtsgAaPjE",
"6332b995efbaf5fe10318169" : "AhAtPadYNQPWRsBa6SGwMRi6",
"6332b916efbaf5fe1030f770" : "EAcPFtLxQcisueP95X4kYJ9J",
"6332b9157136995018bfd2b1" : "vbgG13yWePi44ZDbb6Zee6vi",
"633bad706aedf282fd8d1204" : "ucYKLDahC2mCjUKLBYkg6q9j",
"6332b90f5905bf37c3e6baa9" : "8p6fWM5dBy6NBh9ucxy6hGT7",
"6332b9107136995018bfd143" : "7pTxpweygXM2FWgzwu3CVpPN",
"633badcd1ea08d81f4bdb99a" : "HXGC3EJyWGGd1fKqhLXeX8sL",
"6332b90d5905bf37c3e6ba12" : "1VPZVdTghw3xCQrVunYfdS8J",
"6332b90e88318d0df3ddfcde" : "b9vVZJTyobzvvUvFvLKzZNRT",
"6332b90de27ec8b08cea04df" : "iFX1WPhT1rAs1Lgjk1Yhxqm3",
"6332b9145905bf37c3e6bb5d" : "7YhqMtfLF37quGR5Mf67VZ73",
}


account = "62fc44dc934376949a733248"

query = pcli.channelLinks.list_all(q={"account" : account , "channel" : 10154})


# add what is set in the mapping sheet
for link in query:
    if link.channelSettings.channelLocationId == "TO BE ADDED":
        _id = link.get('_id')
        if link.location != "62fc45091f35f30489effd65":
            print(_id)
            print(str(importTable.get(_id,"TO BE ADDED")))
            pcli.channelLinks.update(link,{
                "channelSettings.channelLocationId" :  str(importTable.get(_id,"TO BE ADDED"))
            })
        else:
            print("north sydney it got stopped")



# call the register api and activate api
regactivate = pcli.channelLinks.list_all(q={"account" : account , "channel" : 10154})
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjQ3OTEyMjUsImV4cCI6MTY2NDg3NzYyNSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.i0Z2w_0GcpYJDvH9oNkTQMpy1O4DjE__8C7NQxAb6Dx7GZQ8OtiHVIx3Mtg01gZCY5EL8xJyFZdlg6HJnJB45i8ZSc8N-C70Ws3pZ-OjENGtkcOV5QR6Gr06wJYhdUkgJL8JIrdPn_hT09vbeHY6LkMaDMtL0Pv36NrLAJrCofHokTyVDFG_A1ZwHy9OVGjVfBv4G1Kvf0bKa6Z3s0GEC10QHFcjoUCphzy93Wg4h6YkRKaq4PD9_dFnOR_6oBflgz5X3sPC-5sLPPx6m6kNIyAY3dccBh0nDULx6N0sU3mFJywUlAPv1mi4sTCjRE_-AY-e5tyYpLp6AnAgNe-EbA"
for vibe in regactivate:
    key = vibe.channelSettings.channelLocationId
    if key != "TO BE ADDED" :
        if vibe.location != "62fc45091f35f30489effd65":
            url = f"https://api.deliverect.com/registerChannelLink/{vibe._id}"
            payload={}
            headers = {
  'Authorization': f'Bearer {token}'
}            
            response = requests.request("POST", url, headers=headers, data=payload)
            
            print(response.text)
            print(vibe._id , "has been registereed")
            time.sleep(2)

            second_url= f"https://api.deliverect.com/activateChannelLink/{vibe._id}"
            second_response = requests.request("POST", second_url, headers=headers, data=payload)
            print(response.text)
            print(vibe._id , "has been activated")
            time.sleep(2)












