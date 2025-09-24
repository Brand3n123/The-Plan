class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Please enter a valid amount to deposit")

    def withdraw(self, amount):
        if amount <= self.balance:
            if amount > 0:
                self.balance -= amount
        else:
            print("Insufficient funds!")

account1 = BankAccount("Branden", 10)
account2 = BankAccount("Alex")

account1.deposit(10)
account1.withdraw(5)
print(account1.balance)