from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db = client["company"]
collection = db["customers"]

# $SET UPDATE OPERATOR
# address alanı 'M' ile başlayan müşterilerin 'name' alanını 'Minnie' yap
query = {"address": {"$regex": r"^M"}}
update = {"$set": {"name": "Minnie"}}
result = collection.update_many(query, update)
print("Eşleşen Dokümanların Sayısı:", result.matched_count)
print("Değiştirilen Dokümanların Sayısı:", result.modified_count)


# $INC UPDATE OPERATOR
# Maaşı 55000'den az olanların maaşlarını 5300 artıralım
query = {"salary": {"$lte": 55_000}}
update = {"$inc": {"salary": 5300}}
result = collection.update_many(query, update)
print("Eşleşen Dokümanların Sayısı:", result.matched_count)
print("Değiştirilen Dokümanların Sayısı:", result.modified_count)

# Maaşı 58500'den yüksek olanların maaşını 5300 azaltalım.
query = {"salary": {"$gt": 58_500}}
update = {"$inc": {"salary": -5300}}
result = collection.update_many(query, update)
print("Eşleşen Dokümanların Sayısı:", result.matched_count)
print("Değiştirilen Dokümanların Sayısı:", result.modified_count)

# $RENAME UPDATE OPERATOR
# salary alanının ismini 'income' olarak değiştirin.
query = {}
update = {"$rename": {"salary": "income"}}
result = collection.update_many(query, update)
print("Eşleşen Dokümanların Sayısı:", result.matched_count)
print("Değiştirilen Dokümanların Sayısı:", result.modified_count)

client.close()