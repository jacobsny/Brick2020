import requests, json, math

api_key = "c61ca7f29dcc434b92c9dadfe6014c73"


# Given a SKU it will return the details of that product from Wegmans API
def getDataBySku(sku):

    data = requests.get("https://api.wegmans.io/products/" + str(sku) + "?api-version=2018-10-18&Subscription-Key=" + api_key)

    return json.loads(data.text)

# Given a SKU it will return the average price from across all Wegmans stores
def getAvgPriceBySku(sku):

    json_str = requests.get("https://api.wegmans.io/products/" + str(sku) + "/prices?api-version=2018-10-18&Subscription-Key=" + api_key)

    data = json.loads(json_str.text)

    prices = []
    for store in data["stores"]:
        prices.append(store['price'])

    average = math.fsum(prices)/len(prices)
    average_price = round(average, 2)

    return average_price

# Given a keyword it will return all the results containing that word or related products.
def getItemsByKeyword(keyword):

    json_str = requests.get("https://api.wegmans.io/products/search?query=" + keyword + "&api-version=2018-10-18&subscription-key=" + api_key)

    data = json.loads(json_str.text)

    return data
