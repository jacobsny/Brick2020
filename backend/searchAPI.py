import requests
import json
import csv, datetime, random

from pymongo import MongoClient

url = "https://api.wegmans.io/products/"
client = MongoClient("mongodb+srv://ccocktail:JacobIsAnAlcoholic@constellationcocktails-iu1cp.mongodb.net/test?retryWrites=true&w=majority")
db = client.constellation


def list_cocktails():
    data = db.cocktails.distinct("Name")
    return data

def get_random():
    boozes = ["Vodka", "Brandy", "Whiskey", "Bourbon", "Tequila", "Brandy", "Rum", "Modelo", "Wine", "Lager", "Beer"]
    type = boozes[random.randint(0, len(boozes)-1)]
    return search_results(type)


def valid_search(keywords):
    list = db.weggies.distinct("varietal") + db.products.distinct("Brand")
    for i in range(0,len(list)):
        list[i] = list[i].lower()
    for keyword in keywords.lower().split():
        for typeWord in list:
            if keyword in typeWord:
                return True
    for cocktail in list_cocktails():
        for word in keywords.split():
            if word.lower() in cocktail.lower() and word.lower() != "and" and word.lower() != "the":
                return True
    return False
    # Is search valid in constellations and cocktailDB?
    # returns a boolean if valid

def get_cocktail(name):
    cursor = db.cocktails.find({"Name": name})
    for cocktail in cursor:
        del cocktail["_id"]
        ingredients = []
        new = {}
        for key in cocktail:
            if "ingredient" in key.lower():
                if "(None, None)" not in cocktail[key]:
                    ingredients.append(cocktail[key])
            elif "Name" == key or "Directions" == key:
                new[key] = cocktail[key]
        new["Ingredients"] = ingredients
        return new


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
            if keyword in product["Varietal"].lower() or keyword in product["DigitalCatalogProductName"].lower().split():
                id_drop_prod = product
                del(id_drop_prod["_id"])
                productsFound.append(id_drop_prod)
                break
    for cocktail in cocktails:
        for keyword in keyList:
            if keyword in cocktail["Name"].lower() or keyword in cocktail["Ingredient1"].lower():
                id_drop_ctail = cocktail
                del(id_drop_ctail["_id"])
                cocktailsFound.append(id_drop_ctail)
                break
    return {"products": productsFound, "cocktails": cocktailsFound}
    # dict = {"products": ["hey this works"]}
    # print(productsFound)
    # print(cocktailsFound)


def search_all():
    products = list(db.products.find({}))
    cocktails = list(db.cocktails.find({}))
    productFinal = []
    for pro in products:
        del pro["_id"]
        productFinal.append(pro)
    cocktailFinal = []
    for cocktail in cocktails:
        del cocktail["_id"]
        cocktailFinal.append(cocktail)
    return {"products": productFinal, "cocktails": cocktailFinal}


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
    count = len(list(cursor))
    return {"Name": name, "Frequency": count}


def get_stats_cocktails(name):
    cursor = db.stats_cocktails.find({"Name": name})
    # TODO return the info from the cursor in the format you need
    count = len(list(cursor))
    return {"Name": name, "Frequency": count}


if __name__ == '__main__':
    # print(valid_search("Corona"))
    # print(stats_product("Modelo Especial Mexican Lager Beer, 6 pk 12 fl oz Cans, 4.4% ABV"))
    # print(get_stats_product("Modelo Especial Mexican Lager Beer, 6 pk 12 fl oz Cans, 4.4% ABV"))
    # print(search_all())
    # print(get_random())

    print(get_cocktail("After sex"))

