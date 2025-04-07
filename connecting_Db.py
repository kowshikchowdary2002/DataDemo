import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bike_wala"
)

cursor=db.cursor()

cursor.execute("SELECT * from bike_wala.bike")

for row in cursor:
    print(row)
