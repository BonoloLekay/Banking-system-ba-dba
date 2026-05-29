from app.customers import create_customer
from app.accounts import create_account
from app.transactions import deposit, withdraw, view_balance

def menu():
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. View Balance")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            create_customer()

        elif choice == "2":
            create_account()

        elif choice == "3":
            deposit()

        elif choice == "4":
            withdraw()

        elif choice == "5":
            view_balance()

        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()