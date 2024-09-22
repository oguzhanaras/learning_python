from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)

# db olustur
db = client["company"]
# koleksiyon olustur
collection = db["customers"]

# sort dokumanları varsayılan olarak artan sekilde sıralar
results = collection.find({}, {"_id": 0, "address": 0}).sort("salary")
for result in results:
    print(result)

# azalan sıralama
results = collection.find({}, {"_id": 0, "address": 0}).sort("salary", -1)
for result in results:
    print(result)

client.close()
