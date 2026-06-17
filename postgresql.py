import psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        database="r1",
        user="postgres",
        password="1234"
    )

    cursor = conn.cursor()

    while True:
        print("\n------ STUDENT ADMINISTRATION ------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search by ID")
        print("4. Search by Name")
        print("5. Update Department")
        print("6. Delete Student")
        print("7. Count Students")
        print("8. Sort by Name")
        print("9. Highest Age")
        print("10. Students by Department")
        print("11. Average Age")
        print("12. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                name = input("Name: ")
                age = int(input("Age: "))
                dept = input("Department: ")

                cursor.execute(
                    "INSERT INTO student(name,age,department) VALUES(%s,%s,%s)",
                    (name, age, dept)
                )
                conn.commit()
                print("Student Added Successfully")

            elif choice == 2:
                cursor.execute("SELECT * FROM student")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            elif choice == 3:
                sid = int(input("Enter ID: "))
                cursor.execute("SELECT * FROM student WHERE id=%s", (sid,))
                row = cursor.fetchone()
                print(row)

            elif choice == 4:
                name = input("Enter Name: ")
                cursor.execute("SELECT * FROM student WHERE name=%s", (name,))
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            elif choice == 5:
                sid = int(input("Enter ID: "))
                dept = input("New Department: ")
                cursor.execute(
                    "UPDATE student SET department=%s WHERE id=%s",
                    (dept, sid)
                )
                conn.commit()
                print("Updated")

            elif choice == 6:
                sid = int(input("Enter ID: "))
                cursor.execute("DELETE FROM student WHERE id=%s", (sid,))
                conn.commit()
                print("Deleted")

            elif choice == 7:
                cursor.execute("SELECT COUNT(*) FROM student")
                print("Total Students =", cursor.fetchone()[0])

            elif choice == 8:
                cursor.execute("SELECT * FROM student ORDER BY name")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            elif choice == 9:
                cursor.execute("SELECT MAX(age) FROM student")
                print("Highest Age =", cursor.fetchone()[0])

            elif choice == 10:
                dept = input("Department: ")
                cursor.execute(
                    "SELECT * FROM student WHERE department=%s",
                    (dept,)
                )
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            elif choice == 11:
                cursor.execute("SELECT AVG(age) FROM student")
                print("Average Age =", round(cursor.fetchone()[0],2))

            elif choice == 12:
                print("Program Ended")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Please enter numbers only.")

except Exception as e:
    print("Connection Error:", e)

finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()