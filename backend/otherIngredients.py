import csv, json
import backend.wegmans as weg

def getIngredients(cocktailList):
    target = cocktailList[4:]

    ingredients = []

    for ingredient in target:
        if "None" not in ingredient:
            ingredients.append(ingredient)

    return ingredients

def getIngredientsPrices(ingredients):

    ingredientsWithPrices = {}

    for ingredient in ingredients:
        name,qnty = ingredient[1:-1].split(",")
        qnty = qnty.strip()

        result = weg.getItemsByKeyword(name)

        if result["pages"] != 0:
            sku = result["results"][0]["sku"]

            price = weg.getAvgPriceBySku(sku)

            ingredientsWithPrices[name] = price


    return ingredientsWithPrices
