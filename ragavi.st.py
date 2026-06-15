import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1122",
    database="r1"
)

cursor = conn.cursor()
while True:
    print("\n----- STUDENT ADMINISTRATION -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search by ID")
    print("4. Search by Name")
    print("5. Update Department")
    print("6. Delete Student")
    print("7. Count Students")
    print("8. Sort by Name")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")

        query = "INSERT INTO students(name, age, department) VALUES (%s, %s, %s)"
        values = (name, age, dept)

        cursor.execute(query, values)
        conn.commit()
        print("Student Added Successfully!")

    elif choice == 2:
        query = "SELECT * FROM students"
        cursor.execute(query)

        records = cursor.fetchall()

        for row in records:
            print(row)

    elif choice == 3:
        sid = int(input("Enter Student ID: "))

        query = "SELECT * FROM students WHERE id=%s"
        values = (sid,)

        cursor.execute(query, values)

        record = cursor.fetchone()

        if record:
            print(record)
        else:
            print("Student Not Found")

    elif choice == 4:
        name = input("Enter Name: ")

        query = "SELECT * FROM students WHERE name=%s"
        values = (name,)

        cursor.execute(query, values)

        records = cursor.fetchall()

        for row in records:
            print(row)

    elif choice == 5:
        sid = int(input("Enter Student ID: "))
        dept = input("Enter New Department: ")

        query = "UPDATE students SET department=%s WHERE id=%s"
        values = (dept, sid)

        cursor.execute(query, values)
        conn.commit()

        print("Student Updated Successfully!")

    elif choice == 6:
        sid = int(input("Enter Student ID: "))

        query = "DELETE FROM students WHERE id=%s"
        values = (sid,)

        cursor.execute(query, values)
        conn.commit()

        print("Student Deleted Successfully!")

    elif choice == 7:
        query = "SELECT COUNT(*) FROM students"
        cursor.execute(query)

        count = cursor.fetchone()

        print("Total Students =", count[0])

    elif choice == 8:
        query = "SELECT * FROM students ORDER BY name ASC"
        cursor.execute(query)

        records = cursor.fetchall()

        for row in records:
            print(row)

    elif choice == 9:
        break

    else:
        print("Invalid Choice")

cursor.close()
conn.close()