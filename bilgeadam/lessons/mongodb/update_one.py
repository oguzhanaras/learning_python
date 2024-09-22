from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db = client["company"]
collection = db["customers"]

# Spesifik bir adresi bulup güncelleyelim
query = {"address": "Valley 345"}    # filtreliyoruz
update = {"$set": {"address": "Canyon 123"}}  # Yeni değer Canyon 123 olarak güncellenecek
result = collection.update_one(query, update)
print("Eşleşen dokümanların sayısı:", result.matched_count)
print("Değiştirilen dokümanların sayısı:", result.modified_count)

client.close()
