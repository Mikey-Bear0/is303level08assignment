# BankAccount class definition

class BankAccount:
    # Initialize the BankAccount with customer name, account number, and starting balance of $0.00
    def __init__(self, customer_name, account_number):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = 0.00

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount

    # Method to withdraw money from the account, ensuring sufficient funds are available
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    # Method to get account information, including customer name, account number, and current balance
    def get_account_info(self):
        return f"Name: {self.customer_name}\nAccount #: {self.account_number}\nBalance: ${self.balance:.2f}"