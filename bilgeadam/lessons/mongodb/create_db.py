from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)

# db olustur
db = client["company"]
# koleksiyon olustur
collection = db["customers"]

print(collection)

print(client.list_database_names())
