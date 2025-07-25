import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sarvesh@123',
    database='emp'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM test_table")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
