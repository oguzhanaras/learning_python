from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db = client["company"]
collection = db["customers"]

query = {"income": {"$gt": 55_000}}
projection = {"_id": 0, "name": 1, "income": 1}

results = collection.find(query, projection).sort("income", -1).limit(5)
for result in results:
    print(result)

# Query: name field'ı [A-L]
# income 55000'den az olan dokümanları income field'ı 2700 artırın.
# 55000'den büyük olanları ise 1.03 ile çarpın
# lastModified field'ını güncelleyin.
# Tüm dökumanları income field'ına göre azalan formda yazdırın, projection: name, income, limit(5)

query1 = {
    "name": {"$regex": "^[A-L]"},
    "income": {"$lte": 55_000}
}

query2 = {
    "name": {"$regex": "^[A-L]"},
    "income": {"$gt": 55000}
}

update1 = {
    "$inc": {"income": 2700},
    "$currentDate": {"lastModified": True}
}

update2 = {
    "$mul": {"income": 1.03},
    "$currentDate": {"lastModified": True}
}

result2 = collection.update_many(query2, update2)
result1 = collection.update_many(query1, update1)

print("Group 1 modified count", result1.modified_count)
print("Group 2 modified count", result2.modified_count)


# Tüm dökumanları income field'ına göre azalan formda yazdırın, projection: name, income, limit(5)
query = {}
projection = {"_id": 0, "name": 1, "income": 1}

results = collection.find(query, projection).sort("income", -1).limit(5)

for result in results:
    print(result)


