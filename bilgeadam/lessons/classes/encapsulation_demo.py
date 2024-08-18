from datetime import datetime


class BankAccount:

    def __init__(self,name, balance=0):
        self.name = name
        self.__balance = balance
        self.__transactions = [f"{self.__generate_datetime()} - opened balance: {self.__balance}"]

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def depozit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"{self.__generate_datetime()} deposited: {amount}")
            print(f"depozited ${amount}. balance: {self.__balance}")
        else:
            print("invalid")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"{self.__generate_datetime()} withdrawn ${amount}")
            print(f"withdrawn ${amount}.. balance: {self.__balance}")
        else:
            print("insufficient balance")

    def __generate_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


account1 = BankAccount("elon musk")
print(account1.name)
account1.get_balance()
account1.get_transactions()

account1.depozit(50)
account1.withdraw(100)
account1.depozit(500)
account1.withdraw(255)

account1.get_transactions()

account2 = BankAccount("jeff bezos", 100000)
account2.depozit(1000)
account2.withdraw(5000)

account2.get_transactions()