from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)

# db olustur
db = client["company"]
# koleksiyon olustur
collection = db["customers"]

# bir sorgu olmaksızın find
my_docs = collection.find()
print(my_docs)

print("all document")
for doc in my_docs:
    print(doc)

# bir sorgu ile find
my_filter = {
    "salary": 50_000
}

my_docs = collection.find(my_filter)

for doc in my_docs:
    print(doc)


# filter ve projection beraber kullanımı
my_filter = {"salary": 50_000}
projection = {"name": 1, "salary": 1} # field secimi
my_docs = collection.find(my_filter, projection)

for doc in my_docs:
    print(doc)


# field haric tutma
my_filter = {"salary": 50_000}
projection = {"name": 1, "salary": 1, "_id": 0} # field secimi
my_docs = collection.find(my_filter, projection)

for doc in my_docs:
    print(doc)

client.close()