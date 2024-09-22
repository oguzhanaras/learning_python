from bson import ObjectId
from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db = client["company"]
collection = db["customers"]

query = {"address": "Mountain 21"}
result = collection.delete_one(query)
print("Deletion Acknowledged:", result.acknowledged)
print("Number of Documents Deleted", result.deleted_count)

# delete_one() query ile eşleşen ilk dokümanı siler.
# Spesifik bir dokümanı silmek için _id alanı query'de kullanılmalıdır

result = collection.delete_one({"_id": 2})
print("Number of Documents Deleted", result.deleted_count)

# ObjectId() ile tanımlanan bir dokümanı silmek
object_id = ObjectId("66eeb0ae64d44bf625caff5f")
result = collection.delete_one({"_id": object_id})
print("Number of Documents Deleted", result.deleted_count)

# Bir belgeyi bulmak (find_one) ve aynı zamanda bu belgeyi silmek (delete_one)
object_id = ObjectId("66eeb1b064d44bf625caff61")
result = collection.find_one_and_delete({"_id": object_id})
print(result)
print(result.keys())

client.close()
