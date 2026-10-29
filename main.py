# Michael Cunningham
# IS 303 Level 08 Assignment
# 10/27/26

import bank_account
import random

# Function to handle choices 1-3
def handle_account_option(choice, account):
    if choice == '1':
        # Validate input to be a numeric value and greater than 0
        while True:
            try:
                deposit_amount = float(input("How much would you like to deposit? "))
                if deposit_amount <= 0:
                    print("Please enter a valid amount greater than 0.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        account.deposit(deposit_amount)
        print(f"${deposit_amount:.2f} deposited successfully.")
    elif choice == '2':
        # Validate input to be a numeric value and greater than 0
        while True:
            try:
                withdraw_amount = float(input("How much would you like to withdraw? "))
                if withdraw_amount <= 0:
                    print("Please enter a valid amount greater than 0.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        account.withdraw(withdraw_amount)
    elif choice == '3':
        print(account.get_account_info())


print("Welcome to the Bank of Michael!")
customer_name = input("Please enter your name: ")
account_number = random.randint(10000, 99999)
account = bank_account.BankAccount(customer_name, account_number)

while True:
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")

    choice = input()

    if choice in ('1', '2', '3'):
        handle_account_option(choice, account)
    elif choice == '4':
        print("Thank you for your business!")
        break
    else:
        print("Invalid choice. Please try again.")
