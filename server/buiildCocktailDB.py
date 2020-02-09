from pymongo import MongoClient
import csv

client = MongoClient(port=27017)
db = client.constellation

# descrip = [a["DigitalCatalogProductName"] for a in list(cursor) if a["BeverageSegment"] == "Spirits"]
boozes = ["Vodka", "Brandy", "Whiskey", "Bourbon", "Tequila", "Brandy", "Rum", "Modelo", "Wine", "Lager", "Beer"]

with open("/home/jacobsny/PycharmProjects/Brick2020/data/cocktails.csv") as cocktails:
    csv_reader = csv.reader(cocktails)
    count = 0
    header = []
    for row in csv_reader:
        if count == 0:
            header = row
        else:
            cock = {}
            for i in range(0, len(header)):
                key = header[i]
                value = row[i]
                cock[key] = value
            ingre = row[3:18]
            constBrand = False
            for ingredient in ingre:
                item = tuple(ingredient[1:-1].split(", "))[0]
                if item != "None":
                    # print(item)
                    for booze in boozes:
                        if booze.lower() in item.lower():
                            constBrand = True
            if constBrand:
                db.cocktails.insert_one(cock)
        count += 1
cursor = db.cocktails.find({})
for row in cursor:
    print(row)