from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)
db = client["company"]
collection = db["customers"]

# bir dokuman olusturmak
mydict = {
    "name": "john",
    "address": "highway 37",
    "salary": 50_000
}

# kolekyisyona bir dokuman ekleme
mydoc = collection.insert_one(document=mydict)
print(mydoc)

mydict2 = {
    "name": "peter",
    "address": "lowstreet 57",
    "salary": 60_000
}

mydoc = collection.insert_one(document=mydict2)

client.close()
