import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="794719",
    database="mydatabase"
)

cursor = mydb.cursor()


# insert into
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)

mydb.commit() # değişiklikleri kaydetmek için commit kullanılmalıdır.

print(cursor.rowcount, "record inserted.")



# insert multiple   executemany
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val)

mydb.commit()

print(cursor.rowcount, "was inserted.")

print("1 record inserted, ID:", cursor.lastrowid)