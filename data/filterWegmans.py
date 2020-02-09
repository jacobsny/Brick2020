import time
import requests
import csv
import json
url_pt1 = "https://api.wegmans.io/products/categories/"
url_pt2 = "?api-version=2018-10-18&subscription-key=c61ca7f29dcc434b92c9dadfe6014c73"
unfiltered_skus = {}


def filter_constel(sku_list):
    filtered = {}
    for category in unfiltered_skus:
        filtered.update({category: []})
        for sku in unfiltered_skus[category]:
            if valid_sku(sku):
                filtered[category].append(sku)
    return filtered


def valid_sku(sku):
    product_info = requests.get("https://api.wegmans.io/products/" + str(sku) + "?api-version=2018-10-18&subscription-key=c61ca7f29dcc434b92c9dadfe6014c73").text

    return False


def get_unfiltered():
    category_list = json.loads(requests.get(url_pt1 + "6941" + url_pt2).text)["categories"]
    for category in category_list:
        iterate_category(category["id"])
    return


def iterate_category(id):
    subcategories = json.loads(requests.get(url_pt1 + id + url_pt2).text)
    name = subcategories["name"]
    if len(subcategories["categories"]) and id != "6941-2521-2615" != 0:
        for category in subcategories["categories"]:
            iterate_category(category["id"])
    else:
        unfiltered_skus.update({name: []})
        for product in subcategories["products"]:
            unfiltered_skus[name].append(product["sku"])
            time.sleep(0.5)
        return
