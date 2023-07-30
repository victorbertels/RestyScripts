#Find prod that are used in the menu
from typing import List

acc = '61a96a8452aaa78db208617c'
menus = pcli.channelMenus.list_all(q={'account':acc})
accountProducts = pcli.products.list_all(q={'account':acc})
prodsInMenu = []

def iterate(queryList):
    global ListSubProducts
    ListSubProducts = []
    prods = pcli.products.list_all(q={'_id':{'$in':queryList}})
    for prod in prods:
        prodsInMenu.append({'_id' : prod._id,'name':prod.name,'plu':prod.plu})
        if getattr(prod,'subProducts', None):
            ListSubProducts.extend(prod.subProducts)

# Iterate through channelMenus' subproducts 
for m in menus:
    i = 0
    categories = pcli.channelCategories.list_all(q={'account':acc,'menu':m._id})
    ListSubProducts = []
    for category in categories:
        if getattr(category,'subProducts',None):
            ListSubProducts.extend(category.subProducts)

    while(len(ListSubProducts) > 0 and i <= 6):
        iterate(ListSubProducts)
        i += 1

    print(f'menu {m.name} fait')

#Remove duplicates
listNoDuplicates = [dict(t) for t in {tuple(sorted(d.items())) for d in prodsInMenu}]

#Print results
print(f'\n -------------------------------------------------- \nNumber of products in menus (inc. duplicates) : {len(prodsInMenu)} items\n\
Number of unique products in menus (no duplicates): {len(listNoDuplicates)} items \n')

# Which products are in 0 menu ?
listIdsMenu = [d['_id'] for d in listNoDuplicates]
listIdsProducts = [d['_id'] for d in accountProducts]
    # ^ results in the items unique to each list  (in this case, we know all items are in listIdsProducts already)
prodsInNoMenu = list(set(listIdsMenu) ^ set(listIdsProducts))

print(f'\n{len(prodsInNoMenu)} products are not in a menu \n' + 'Do you want to print the list? y or press Enter')
x = input()
if x == "y":
    print(*prodsInNoMenu, sep = "\n")

#Write in a csv ? 
print('Want to export the products in menus to a CSV? y or press Enter')
y = input()
if y == "y":
    import csv
    with open('products_in_menu.csv', mode='w') as csv_file:
        fieldnames = ['_id', 'name', 'plu']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in listNoDuplicates:
            writer.writerow(i)