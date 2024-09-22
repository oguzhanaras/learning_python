from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db = client["tech"]

# KOLEKSİYON DÜŞÜRMEK
collection_name = input("Silinecek koleksiyon adını giriniz: ")
if collection_name in db.list_collection_names():
    db[collection_name].drop()
    print(f"{collection_name} isimli koleksiyon silindi.")
else:
    print(f"{collection_name} isimli bir koleksiyon mevcut değil.")

# DATABASE SİLMEK
db_name = input("Silinecek veritabanının ismini giriniz: ")
if db_name in client.list_database_names():
    client.drop_database(db_name)
    print(f"{db_name} isimli database silindi.")
else:
    print(f"{db_name} isimli bir database mevcut değil.")

client.close()