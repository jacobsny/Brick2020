from pymongo import MongoClient
import csv

client = MongoClient(port=27017)
db = client.constellation

with open("/home/jacobsny/PycharmProjects/Brick2020/data/Products.csv") as Products:
    csv_reader = csv.reader(Products)
    count = 0
    header = []
    for row in csv_reader:
        if(count == 0):
            header = row
            print(header)
        else:
            product = {}
            for i in range(0,len(header)):
                key = header[i]
                value = row[i]
                product[key] = value
            db.products.insert_one(product)
        count += 1
cursor = db.products.find({})
for row in cursor:
    print(row)
