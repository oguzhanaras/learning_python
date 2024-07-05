import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="794719",
    database="mydatabase"
)

mycursor = mydb.cursor()


# select seçim yapar
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall() #fetchall tum satırları getirir

for x in myresult:
    print(x)


# select column = name
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()


for x in myresult:
    print(x)

# fetchone ilk satırı getirir
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)