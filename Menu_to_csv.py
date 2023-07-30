import os
import json
import csv

from datetime import datetime as dt


local_path = os.path.dirname(os.path.abspath(__file__))
modifier_group_IDs = set()
modifier_IDs = set()


def get_data(path):
    dataset_list = []
    for json_file in os.listdir(path):
        if json_file.endswith(".json"):
            with open(os.path.join(path, json_file), "r") as f:
                content = f.read()
                data = json.loads(content)
                dataset_list.append(data)
    return dataset_list[0]


def get_menu_items(dataset_menu_items):
    all_menu_items = []
    for item in dataset_menu_items["menu"]["menu_items"]:
        if item["id"] in modifier_IDs:
            type = "MODIFIER"
        else:
            type = "PRODUCT"

        single_item = {
            "id": item.get("id"),
            "name": item.get("name"),
            "description": item.get("description"),
            "price": item.get("price"),
            "type": type
        }
        if item.get("modifier_group_ids"):
            modifier_group_IDs.update(item["modifier_group_ids"])
        all_menu_items.append(single_item)
    return all_menu_items


def get_menu_categories(dataset_menu_categories):
    all_menu_categories = []
    for category in dataset_menu_categories["menu"]["menu_categories"]:
        single_category = {
            "id": category.get("id"),
            "name": category.get("name"),
            "description": category.get("description"),
            "type": "CATEGORY"
        }
        all_menu_categories.append(single_category)
    return all_menu_categories


def get_menu_modifier_groups(dataset_menu_mod_groups):
    all_menu_modifier_groups = []
    for mod_gr in dataset_menu_mod_groups["menu"]["menu_modifier_groups"]:
        single_mod_gr = {
            "id": mod_gr.get("id"),
            "name": mod_gr.get("name"),
            "type": "MODIFIER_GROUP"
        }
        if mod_gr.get("modifier_item_ids"):
            modifier_IDs.update(mod_gr["modifier_item_ids"])
        all_menu_modifier_groups.append(single_mod_gr)
    return all_menu_modifier_groups


def convert_to_csv(all_data, file_name=None):
    keys = set()
    for a in all_data:
        keys_list = [a for a in a.keys()]
        keys.update(keys_list)
    if not file_name:
        file_name = str(dt.now())
    with open(os.path.join(local_path, f"{file_name}.csv"), "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_data)


if __name__ == "__main__":
    raw_data = get_data(path=local_path)
    categories = get_menu_categories(raw_data)
    modifier_groups = get_menu_modifier_groups(raw_data)
    products = get_menu_items(raw_data)
    all_data = []
    all_data.extend(categories + modifier_groups + products)
    convert_to_csv(all_data)
