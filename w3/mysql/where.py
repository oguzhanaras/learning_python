import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="794719",
    database="mydatabase"
)

mycursor = mydb.cursor()


# where filtrelemeye yarar
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# Ayrıca, belirli bir harf veya ifadeyle başlayan, içeren veya biten kayıtları da seçebilirsiniz.
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
    print(x)

# sqlite injection
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)