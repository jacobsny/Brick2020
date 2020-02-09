import backend.wegmans as weg


# Given a cocktail from cocktails.csv it will return a list of ingredients
def getIngredients(cocktailList):
    target = cocktailList[4:]

    ingredients = []

    for ingredient in target:
        if "None" not in ingredient:
            ingredients.append(ingredient)

    return ingredients

# Given a list of ingredients it will return a dictionary with the ingredients mapping the prices using the Wegmans API
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

# Given a dictionary of ingredients mapped to price it will return the total price of all the other ingredients
def pricePerServing(dic):
    price = 0

    for value in dic.keys():
        price += value

    return price
