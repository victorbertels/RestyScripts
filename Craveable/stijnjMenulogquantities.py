for menu in menulogJson["menus"]:
    categories = menu.get("categories")
    for category in categories:
        products = category.get("items")
        for product in products:
            modifiers = product.get("modifiers")
            for modifier in modifiers:
                pick = modifier.get("pick", {})
                min = pick.get("range", {}).get("from", 0)
                exactly = pick.get("exactly", 0)
                # print(f"{min}, {exactly} and {len(modifiers)}")
                if min > len(modifiers.get("options")):
                    print(f"{modifier['name']} has minimum {min} greater than {len(modifiers)}")
                if exactly > len(modifiers):
                    print(f"{modifier['name']} has exactly {exactly} greater than {len(modifiers)}")