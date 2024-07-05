import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="794719",
    database="mydatabase"
)

cursor = mydb.cursor()

# create table
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)


# alter table gunceller
cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)