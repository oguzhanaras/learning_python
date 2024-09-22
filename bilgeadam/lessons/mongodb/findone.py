from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)
db = client["company"]
collection = db["customers"]

# bir sorgu olmaksızın find_one
result = collection.find_one()
print(result)

# bir sorgu ile find_one
fltr = {
    "name": "peter"
}

result = collection.find_one(filter=fltr)
print(result)

# farklı alana göre filter
fltr = {
    "address": "Apple st 652"
}

result = collection.find_one(filter=fltr)
print(result)

client.close()