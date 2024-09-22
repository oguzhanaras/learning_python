from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)


db = client["company"]

collection = db["customers"]

# adresi s ile baslayanların hepsini sil
my_filter = {"address": {"$regex": "^S"}}
result = collection.delete_many(my_filter)

print("deletion acknowledged: ", result.acknowledged)
print("number of document deleted:", result.deleted_count)


client.close()