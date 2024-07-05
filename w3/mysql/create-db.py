import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="794719"
)

myCursor = mydb.cursor()

myCursor.execute("CREATE DATABASE mydatabase")
myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)

# Ya da bağlantı kurarken veritabanına erişmeyi deneyebilirsiniz:
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)