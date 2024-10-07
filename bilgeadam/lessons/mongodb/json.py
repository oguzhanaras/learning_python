from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client["nobel"]

# nobelPrizes.json dosyasını yükle
with open("nobelPrizes.json", encoding="utf-8") as file:
    nobel_prizes_data = json.load(file)

print(nobel_prizes_data)
print(type(nobel_prizes_data))

# laureates.json dosyasını yükle
with open("laureates.json", encoding="utf-8") as file:
    laureates_data = json.load(file)

print(laureates_data)

# nobel_prizes isimli koleksiyon oluştur ve dokümanları ekle
nobel_prizes_collection = db["nobel_prizes"]
cursor = nobel_prizes_collection.insert_many(nobel_prizes_data['nobelPrizes'])
print("İşlem Başarılı", cursor.acknowledged)


# laureates isimli koleksiyon oluşturun ve dokümanları ekleyin.
laureates_collection = db["laureates"]
cursor = laureates_collection.insert_many(laureates_data['laureates'])
print("İslem Başarılı", cursor.acknowledged)
print(len(cursor.inserted_ids))

# nobel_prizes koleksiyonundan "Chemistry" kategorisine göre filtreleme sorgusu yazalım.
query = {"category.en": "Chemistry"}
result = nobel_prizes_collection.find_one(query)
print(result)

result["laureates"][0]['knownName']['en']

results = nobel_prizes_collection.find(query)
for result in results:
    print(result['awardYear'], result["laureates"][0]['knownName']['en'])

