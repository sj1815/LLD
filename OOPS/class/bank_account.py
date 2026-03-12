class BankAccount:
    def __init__(self, account_number: str, owner_name: str):
        # Initialize fields: account_number, owner_name, balance (starts at 0)
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = 0.0

    def deposit(self, amount: float) -> None:
        # Add amount to balance (only if amount is positive)
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount: float) -> bool:
        # Remove amount from balance if sufficient funds exist
        # Return True if successful, False otherwise
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True 
        return False

    def get_balance(self) -> float:
        # Return the current balance
        return self._balance


if __name__ == "__main__":
    account = BankAccount("123456", "John Doe")
    account.deposit(1000)
    print(account.get_balance())  # Should print 1000.0

    success = account.withdraw(500)
    print(str(success).lower())   # Should print true
    print(account.get_balance())  # Should print 500.0

    success = account.withdraw(1000)
    print(str(success).lower())   # Should print false