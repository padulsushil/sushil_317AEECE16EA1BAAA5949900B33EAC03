class BankAccount:
    def __init__(self, account_number: str, account_holder_name: str, account_balance: float):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount: float) -> None:
        self.__account_balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__account_balance:
            print("Insufficient balance")
        else:
            self.__account_balance -= amount

    def display_account_balance(self) -> float:
        return self.__account_balance

# Create a BankAccount object
my_account = BankAccount("1234567890", "John Doe", 1000.0)

# Deposit some money
my_account.deposit(500.0)

# Withdraw some money
my_account.withdraw(200.0)

# Display the current account balance
print("Current account balance:", my_account.display_account_balance())
