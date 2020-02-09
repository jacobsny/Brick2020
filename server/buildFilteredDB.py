from pymongo import MongoClient
import csv

client = MongoClient(port=27017)
db = client.constellation
#
# with open("/home/jacobsny/PycharmProjects/Brick2020/data/filtered.csv") as filters:
#     reader = csv.reader(filters)
#     count = 0
#     for row in reader:
#         if count >= 3:
#             if len(row) > 2:
#                 keyword = {"varietal": row[0], "SKU": row[1:]}
#                 db.weggies.insert_one(keyword)
#             else:
#                 keyword = {"varietal": row[0], "SKU": []}
#                 db.weggies.insert_one(keyword)
#         count += 1

cursor = db.weggies.find({})
for row in cursor:
    print(row)