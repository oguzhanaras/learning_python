from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client["pizza"]
collection = db["orders"]

orders = [
    {"_id": 0, "name": "Pepperoni", "size": "small", "price": 19, "quantity": 10, "date": "2021-03-13T08:14:30Z"},
    {"_id": 1, "name": "Pepperoni", "size": "medium", "price": 20, "quantity": 20, "date": "2021-03-13T09:13:24Z"},
    {"_id": 2, "name": "Pepperoni", "size": "large", "price": 21, "quantity": 30, "date": "2021-03-17T09:22:12Z"},
    {"_id": 3, "name": "Cheese", "size": "small", "price": 12, "quantity": 15, "date": "2021-03-13T11:21:39.736Z"},
    {"_id": 4, "name": "Cheese", "size": "medium", "price": 13, "quantity": 50, "date": "2022-01-12T21:23:13.331Z"},
    {"_id": 5, "name": "Cheese", "size": "large", "price": 14, "quantity": 10, "date": "2022-01-12T05:08:13Z"},
    {"_id": 6, "name": "Vegan", "size": "small", "price": 17, "quantity": 10, "date": "2021-01-13T05:08:13Z"},
    {"_id": 7, "name": "Vegan", "size": "medium", "price": 18, "quantity": 10, "date": "2021-01-13T05:10:13Z"},
    {"_id": 8, "name": "Vegan", "size": "medium", "price": 18, "quantity": 15, "date": "2021-01-16T06:10:54Z"},
    {"_id": 9, "name": "Cheese", "size": "medium", "price": 18, "quantity": 22, "date": "2021-01-15T07:11:54Z"},
    {"_id": 10, "name": "Pepperoni", "size": "medium", "price": 18, "quantity": 14, "date": "2021-01-14T08:14:54Z"},
    {"_id": 11, "name": "Pepperoni", "size": "medium", "price": 18, "quantity": 12, "date": "2021-01-15T09:23:54Z"}
]

cursor = collection.insert_many(orders)

# Aggregation Pipeline 1: Toplam sipariş miktarını hesaplayacağız (medium size pizzalar için)
pipeline1 = [
    # Stage 1: Filtreleme
    {"$match": {"size": "medium"}},
    # Stage 2: Gruplama
    {"$group": {"_id": "$name", "totalQuantity": {"$avg": "$quantity"}}}
]

result1 = collection.aggregate(pipeline1)
print(result1)
for result in result1:
    print(result)


orders = [
    {"_id": 12, "name": "Pepperoni", "size": "small", "price": 19, "quantity": 15, "date": "2021-03-13T08:14:30Z"},
    {"_id": 13, "name": "Pepperoni", "size": "medium", "price": 20, "quantity": 25, "date": "2021-03-13T09:13:24Z"},
    {"_id": 14, "name": "Pepperoni", "size": "large", "price": 21, "quantity": 35, "date": "2021-03-17T09:22:12Z"},
    {"_id": 15, "name": "Cheese", "size": "small", "price": 12, "quantity": 20, "date": "2021-03-13T11:21:39.736Z"},
    {"_id": 16, "name": "Cheese", "size": "medium", "price": 13, "quantity": 55, "date": "2022-01-12T21:23:13.331Z"},
    {"_id": 17, "name": "Cheese", "size": "large", "price": 14, "quantity": 15, "date": "2022-01-12T05:08:13Z"},
    {"_id": 18, "name": "Vegan", "size": "small", "price": 17, "quantity": 15, "date": "2021-01-13T05:08:13Z"},
    {"_id": 19, "name": "Vegan", "size": "medium", "price": 18, "quantity": 15, "date": "2021-01-13T05:10:13Z"}
]

# Yeni siparişleri veritabanına ekle
collection.insert_many(orders)


# Aggregation Pipeline 2: Cheese pizzaların boyutlarına göre toplam sipariş miktarını hesapla.
pipeline2 = [
    {"$match": {"name": "Cheese"}},
    {"$group": {"_id": "$size", "totalQuantity": {"$sum": "$quantity"}}}
]
result2 = collection.aggregate(pipeline2)
# print(list(result2))
for result in result2:
    print(result)

# Aggregation Pipeline 3: Belirli bir tarih aralığındaki toplam sipariş değerini ve ortalama sipariş miktarını hesapla
pipeline3 = [
    {"$match": {"date": {"$gte": "2021-03-13T08:14:30Z", "$lte": "2021-12-31T23:59:50Z"}}}, # belirli bir tarih aralığını seç
    {
        "$group": {
            "_id": "$size", # Boyuta göre grupla
            "totalOrderValue": {"$sum": {"$multiply": ["$price", "$quantity"]}}, # Toplam sipariş fiyatı
            "averageOrderQuantity": {"$avg": "$quantity"}   # Ortalama sipariş miktarı
        }
    }
]

result3 = collection.aggregate(pipeline3)
for result in result3:
    print(result)
