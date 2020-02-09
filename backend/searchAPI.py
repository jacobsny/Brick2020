import requests
import json
import csv
import datetime

from pymongo import MongoClient

url = "https://api.wegmans.io/products/"
client = MongoClient(port=27017)
db = client.constellation


def list_cocktails():
    data = db.cocktails.distinct("Name")
    return data


def valid_search(keywords):
    with open("data/filtered.csv") as types:
        reader = csv.reader(types)
        for i in range(0,3):
            for type in next(reader):
                if type.lower() in keywords.lower():
                    return True
    for cocktail in list_cocktails():
        for word in keywords.split():
            if word.lower() in cocktail.lower() and word.lower() != "and" and word.lower() != "the":
                return True
    return False
    # Is search valid in constellations and cocktailDB?
    # returns a boolean if valid


def search_results(keywords):
    products = db.products.find({})
    productsFound = []
    cocktails = db.cocktails.find({})
    cocktailsFound = []
    keyList = keywords.lower().split(" ")
    if "and" in keyList:
        keyList.remove("and")
    if "the" in keyList:
        keyList.remove("the")
    for product in products:
        for keyword in keyList:
            if keyword in product["Varietal"].lower():
                productsFound.append(product)
                break
            if keyword in product["DigitalCatalogProductName"].lower().split():
                productsFound.append(product)
                break
    for cocktail in cocktails:
        for keyword in keyList:
            if keyword in cocktail["Name"].lower() or keyword in cocktail["Ingredient1"].lower():
                cocktailsFound.append(cocktail)
                break
    # return json.dumps({"products": productsFound, "cocktails": cocktailsFound})
    return json.dumps({"products": ["hey this works"]})
    # print(productsFound)
    # print(cocktailsFound)


def stats_product(name):
    now = datetime.datetime.now()
    current = now.strftime("%Y-%m-%d %H:%M:%S")
    db.stats_product.insert_one({"datetime": current, "Name": name})


def stats_cocktails(name):
    now = datetime.datetime.now()
    current = now.strftime("%Y-%m-%d %H:%M:%S")
    db.stats_cocktails.insert_one({"datetime": current, "Name": name})


def get_stats_product(name):
    cursor = db.stats_product.find({"Name": name})
    # TODO return the info from the cursor in the format you need


def get_stats_cocktails(name):
    cursor = db.stats_cocktails.find({"Name": name})
    # TODO return the info from the cursor in the format you need


if __name__ == '__main__':
    print(search_results("bourbon"))
