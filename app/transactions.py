from app.db import get_connection

def deposit():
    account_id = input("Account ID: ")
    amount = float(input("Deposit amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.callproc('Deposit', (account_id, amount))
        conn.commit()
        print("Deposit successful")

    except Exception as e:
        conn.rollback()
        print("Deposit failed:", e)

    finally:
        conn.close()

def withdraw():
    account_id = input("Account ID: ")
    amount = float(input("Withdraw amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Get current balance FIRST
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = %s",
            (account_id, amount)
        )
        result = cursor.fetchone()

        if not result:
            print("Account not found")
            return

        balance = result[0]

        if amount > balance:
            print("Insufficient funds")
            return

        # Call procedure only if valid
        cursor.callproc('withdraw', (account_id, amount))
        conn.commit()

        print("Withdrawal successful")

    except Exception as e:
        conn.rollback()
        print("Withdrawal failed:", e)

    finally:
        conn.close()

def view_balance():
    account_id = input("Account ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM accounts WHERE account_id = %s",
        (account_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        print("Balance:", result[0])
    else:
        print("Account not found")