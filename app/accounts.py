from app.db import get_connection

def create_account():
    customer_id = input("Enter customer ID: ")
    balance = 0

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO accounts (customer_id, balance) VALUES (%s, %s)"
    cursor.execute(query, (customer_id, balance))

    conn.commit()
    conn.close()

    print("Account created successfully. Account ID: ", cursor.lastrowid)