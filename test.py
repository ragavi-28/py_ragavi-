import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1122",
    database="r1"
)

cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

query = "SELECT * FROM users WHERE username=%s AND password=%s"
cursor.execute(query, (username, password))

if cursor.fetchone():
    print("Login Successful")
else:
    print("Invalid Login")

cursor.close()
conn.close()