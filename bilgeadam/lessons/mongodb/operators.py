from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)

# db olustur
db = client["company"]
# koleksiyon olustur
collection = db["customers"]

# ---------- query operators

# $gt >
my_filter = {"address": {"$gt": "Sunset Blvd 123"}}
results = collection.find(my_filter)

print("documents with address gt sunset")
for result in results:
    print(result)


my_filter = {"salary": {"$gt": 50_000}}
projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(my_filter, projection)

print("documents with salary greater than 50_000")
for result in results:
    print(result)


# in operator
my_filter = {
    "address": {
        "$in": ["lowstreet 57", "Ocean blvd 2", "Sideway 1633"]
    }
}

projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(my_filter, projection)

for result in results:
    print(result)


# not in operator
my_filter = {
    "address": {
        "$nin": ["lowstreet 57", "Ocean blvd 2", "Sideway 1633"]
    }
}

projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(my_filter, projection)

for result in results:
    print(result)


# ------------logical
# and
my_filter = {
    "$and": [
        {"name": {"$regex": "[aeiou]$"}},
        {"salary": {"$gt": 55_000}}
    ]
}

projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(my_filter, projection)

for result in results:
    print(result)


my_filter = {
    "$or": [
        {"name": {"$regex": "[aeiou]$"}},
        {"salary": {"$gt": 55_000}}
    ]
}

projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(my_filter, projection)

for result in results:
    print(result)

client.close()