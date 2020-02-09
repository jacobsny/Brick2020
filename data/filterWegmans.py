import time
import requests
import csv
import json
import backend.wegmans as wegmans
url_pt1 = "https://api.wegmans.io/products/categories/"
url_pt2 = "?api-version=2018-10-18&subscription-key=c61ca7f29dcc434b92c9dadfe6014c73"


def get_brands():
    brand_list = []
    with open("Products.csv", newline='') as constel_products:
        reader = csv.reader(constel_products, delimiter=",")
        next(reader)
        # row = next(reader)
        # brand_list.append((row[1],row[0],row[3]))
        for row in reader:
            brand_list.append((row[1], row[0], row[3]))
    return brand_list

def get_products():
    products = {}
    broad_to_specific = {"Beer" : set(), "Wine": set(), "Spirits": set()}
    for brand in get_brands():
        time.sleep(0.5)
        brandname = brand[0]
        print(brandname)
        broad_category = brand[1]
        specific_category = brand[2]
        broad_to_specific[broad_category].add(specific_category)
        products_list = wegmans.getItemsByKeyword(brandname)["results"]
        if len(products_list) > 0:
            if(not specific_category in products):
                products.update({specific_category: []})
            for product in products_list:
                if brandname in product["name"]:
                    products[specific_category].append(product["sku"])
    return (products, broad_to_specific)


def write_csv():
    tuple = get_products()
    products = tuple[0]
    broad_to_specific = tuple[1]
    with open("filtered.csv", "w", newline='') as filtered:
        writer = csv.writer(filtered, delimiter=',')
        for broad in broad_to_specific:
            writer.writerow([broad] + list(broad_to_specific[broad]))
        for product in products:
            writer.writerow([product] + products[product])
    return


if __name__ == '__main__':
    write_csv()

# def valid_sku(sku):
#     product_info = requests.get("https://api.wegmans.io/products/" + str(sku) + "?api-version=2018-10-18&subscription-key=c61ca7f29dcc434b92c9dadfe6014c73").text
#     for brand in brands:
#         if(product_info["brand"].toLowercase in brand[0]):
#             print("fuck")
#     return False


# def get_unfiltered():
#     category_list = json.loads(requests.get(url_pt1 + "6941" + url_pt2).text)["categories"]
#     for category in category_list:
#         iterate_category(category["id"])
#     return
#
#
# def iterate_category(id):
#     subcategories = json.loads(requests.get(url_pt1 + id + url_pt2).text)
#     name = subcategories["name"]
#     if len(subcategories["categories"]) and id != "6941-2521-2615" != 0:
#         for category in subcategories["categories"]:
#             iterate_category(category["id"])
#     else:
#         unfiltered_skus.update({name: []})
#         for product in subcategories["products"]:
#             unfiltered_skus[name].append(product["sku"])
#             time.sleep(0.5)
#         return
#