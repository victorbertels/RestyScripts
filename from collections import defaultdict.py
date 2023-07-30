from collections import defaultdict


acc = '5f3a9a3c1d3f1ba68382d311'
iprods = pcli.products.list_all(q={'account': acc, 'isInternal': True})
# search dupes
countPLUs = defaultdict(list)
for p in iprods:
    countPLUs[p.plu].append(p)
for plu, matches in countPLUs.items():
  for i, match in enumerate(matches[1:]):
     # make all unique and remember for later
     match.plu = f'dup-{i+1}-{match.plu}'
     print(match.plu)
     pcli.products.update(match, {'plu': match.plu})
# create lookup
iprodById = {p._id: p for p in iprods}
# now fix menus
cprods = pcli.channelProducts.list_all(q={'account': acc})
for cprod in cprods:
  iprod = iprodById.get(cprod.deliverectProductId)
  if iprod and iprod.plu != cprod.plu:
      pcli.channelProducts.update(cprod, {'plu': iprod.plu})
  else:
      # not an internal product
      pass