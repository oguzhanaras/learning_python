# Python, MySQL veritabanına erişmek için bir MySQL sürücüsüne ihtiyaç duyar
# "MySQL Connector" yüklemek için PIP kullanmanızı öneririz.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="794719"
)

print(mydb)