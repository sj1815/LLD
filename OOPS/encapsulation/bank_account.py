class BankAccount:
    def __init__(self, account_holder: str):
        self.__account_holder = account_holder
        self.__balance = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self) -> float:
        return self.__balance

    def account_holder(self) -> str:
        return self.__account_holder

if __name__ == "__main__":
    account = BankAccount("ABC")

    account.deposit(500)
    print("Balance after deposit:", account.balance)

    account.withdraw(200)
    print("Balance after withdrawal:", account.balance)

    # Uncomment to test errors
    # account.withdraw(1000)