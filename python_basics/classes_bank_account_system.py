# Создай классы BankAccount и Bank.

# BankAccount:
# owner, balance (float, по умолчанию 0)
# deposit(amount), withdraw(amount), get_balance()

# Bank:
# Хранит список аккаунтов.
# create_account(owner) — создаёт аккаунт, если владельца ещё нет.
# transfer(sender, receiver, amount) — перевод между аккаунтами.
# get_total_balance() — общая сумма всех счетов.
# get_richest_client() — возвращает имя клиента с максимальным балансом.


class BankAccount:

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, float) or amount > 0:
            raise ValueError("Wrong amount")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, float) or amount > 0:
            raise ValueError("Wrong amount")

        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance

    def __repr__(self):
        return f"Account {self.owner}, {self.balance}"

    def __eq__(self, obj):
        if isinstance(obj, BankAccount):
            return self.owner == obj.owner
        return False


class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self, owner: BankAccount):
        if any(account == owner for account in self.accounts):
            raise ValueError("Account already exists")

        self.accounts.append(owner)

    def transfer(self, sender, receiver, amount):
        if amount < 0:
            raise ValueError("Wrong amount")

        if not all((sender in self.accounts, receiver in self.accounts)):
            raise ValueError("Sender or receiver doesn't exist")

        sender.balance -= amount
        receiver.balance += amount
        print(f"{sender} has successfully sent {receiver} {amount}")

    def get_richest_client(self):
        if not self.accounts:
            return None

        return max(self.accounts, key=lambda el: el.balance)


owner_1 = BankAccount("Jake", balance=100.0)
owner_2 = BankAccount("Amy", balance=150.0)
owner_3 = BankAccount("Boyle", balance=150.0)
bank = Bank()

bank.create_account(owner_1)
bank.create_account(owner_2)
print(bank.accounts)
print(bank.get_richest_client())
bank.transfer(owner_2, owner_1, -50)
print(bank.accounts)
