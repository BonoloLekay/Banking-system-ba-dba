from app.db import get_connection

def deposit():
    account_id = input("Account ID: ")
    amount = float(input("Deposit amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.callproc('Deposit',
                   (amount, account_id))

    conn.commit()
    conn.close()

    print("Deposit successful")

def withdraw():
    account_id = input("Account ID: ")
    amount = float(input("Withdraw amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.callproc('Withdraw',
                   (amount, account_id))

    conn.commit()
    conn.close()

    print("Withdrawal successful")

def view_balance():
    account_id = input("Account ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    if result:
        print("Balance:", result[0])
    else:
        print("Account not found")