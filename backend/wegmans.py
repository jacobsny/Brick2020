import requests, json, math

api_key = "c61ca7f29dcc434b92c9dadfe6014c73"

def getDataBySku(sku):

    data = requests.get("https://api.wegmans.io/products/" + str(sku) + "?api-version=2018-10-18&Subscription-Key=" + api_key)

    return json.loads(data.text)

def getAvgPriceBySku(sku):

    json_str = requests.get("https://api.wegmans.io/products/" + str(sku) + "/prices?api-version=2018-10-18&Subscription-Key=" + api_key)

    data = json.loads(json_str.text)

    prices = []
    for store in data["stores"]:
        prices.append(store['price'])

    average = math.fsum(prices)/len(prices)
    average_price = round(average, 2)

    return average_price

def getItemsByKeyword(keyword):

    json_str = requests.get("https://api.wegmans.io/products/search?query=" + keyword + "&api-version=2018-10-18&subscription-key=" + api_key)

    data = json.loads(json_str.text)

    return data





print(getAvgPriceBySku(484208))
print(getItemsByKeyword("Belle Meade Bourbon XO"))

