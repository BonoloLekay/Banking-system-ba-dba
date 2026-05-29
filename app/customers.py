from app.db import get_connection

def create_customer():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO customers (name, surname, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, surname, email))

    conn.commit()
    conn.close()

    print("Customer created successfully", cursor.lastrowid)