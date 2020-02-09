import requests
import json
import csv

from pymongo import MongoClient

url = "https://api.wegmans.io/products/"
client = MongoClient(port=27017)
db = client.constellation


def list_cocktails():
    data = db.cocktails.distinct("Name")
    print(data)
    return data


def valid_search(keywords):
    print(keywords)
    with open("../data/filtered.csv") as types:
        reader = csv.reader(types)
        for i in range(0,3):
            for type in next(reader):
                if type.lower() in keywords.lower():
                    return True
    for word in list_cocktails().split():
        if word.lower() in keywords.lower():
            return True
    return False
    # Is search valid in constellations and cocktailDB?
    # returns a boolean if valid

def search_results(keywords, servings):
    print(keywords,servings)


if __name__ == '__main__':
    print(valid_search("beer"))
