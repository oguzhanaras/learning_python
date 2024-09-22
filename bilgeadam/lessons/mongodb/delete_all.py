from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/"
client = MongoClient(host=conn_str)


db = client["company"]

collection = db["deleted"]

program = {
    "name": "MongoDB",
    "type": "Database",
    "initial_relase": 2009,
    "scalability": "High",
    "performance": "Fast",
    "creator": "MondoDB INC."
}

doc = collection.insert_one(program)

programs = [
    {
        "name": "Python",
        "type": "Programming Language",
        "initial_release": 1991,
        "scalability": "High",
        "performance": "High",
        "creator": "Guido van Rossum"
    },
    {
        "name": "Java",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "High",
        "performance": "Medium",
        "creator": "James Gosling"
    },
    {
        "name": "JavaScript",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Brendan Eich"
    },
    {
        "name": "C++",
        "type": "Programming Language",
        "initial_release": 1985,
        "scalability": "High",
        "performance": "High",
        "creator": "Bjarne Stroustrup"
    },
    {
        "name": "MySQL",
        "type": "Database",
        "initial_release": 1995,
        "scalability": "High",
        "performance": "High",
        "creator": "MySQL AB"
    },
    {
        "name": "Ruby",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Yukihiro Matsumoto"
    },
    {
        "name": "PHP",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Rasmus Lerdorf"
    },
    {
        "name": "TensorFlow",
        "type": "Machine Learning Library",
        "initial_release": 2015,
        "scalability": "High",
        "performance": "High",
        "creator": "Google Brain Team"
    },
    {
        "name": "Apache CouchDB",
        "type": "Database",
        "initial_release": 2005,
        "scalability": "High",
        "performance": "High",
        "creator": "Apache Software Foundation"
    }
]

doc2 = collection.insert_many(programs)

my_filter = {
    "$or": [
        {"type": "Machine Learning Library"},
        {"type": "Database"}
    ]
}
projection = {"_id": 0, "name": 1, "initial_relase": 1}  # field secimi
my_docs = collection.find(my_filter, projection)

for doc in my_docs:
    print(doc)


my_filter = {"type": "Database"}
result = collection.delete_many(my_filter)


my_filter = {}
result2 = collection.delete_many(my_filter)

client.close()
