from datetime import datetime

class BankAccount:
    # Class variable to keep track of all accounts
    all_accounts = []

    # Class variable for the interest rate (a constant shared by all instances)
    interest_rate = 0.02

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.creation_date = datetime.now()
        # Adding the account to the list of all accounts
        BankAccount.all_accounts.append(self)

    @classmethod
    def get_total_balance(cls):
        """Class method to get the total balance of all accounts."""
        total_balance = sum(account.balance for account in cls.all_accounts)
        return total_balance

    @classmethod
    def get_oldest_account(cls):
        """Class method to get the oldest account."""
        oldest_account = min(cls.all_accounts, key=lambda account: account.creation_date)
        return oldest_account

    @staticmethod
    def calculate_interest(balance):
        """Static method to calculate interest for a given balance."""
        # The interest rate is a class variable, so it is accessed using the class name
        interest = balance * BankAccount.interest_rate
        return interest

    def deposit(self, amount):
        """Instance method to deposit money into the account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Instance method to withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# Creating some bank accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)
account3 = BankAccount("Charlie", 500)

# Using class methods
total_balance = BankAccount.get_total_balance()
oldest_account = BankAccount.get_oldest_account()

# Using the static method to calculate interest
interest_on_balance = BankAccount.calculate_interest(1500)

# Displaying results
print(f"Total balance of all accounts: ${total_balance}")
print(f"The oldest account was created by {oldest_account.account_holder} on {oldest_account.creation_date}")
print(f"Interest on balance $1500: ${interest_on_balance}")

# Alternatively, we can use the static method with an instance
interest_on_account1 = BankAccount.calculate_interest(account1.balance)
# Displaying results
print(f"Interest on balance of account1: ${interest_on_account1}")