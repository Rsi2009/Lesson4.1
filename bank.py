class Account():
        def __init__(self, ID, balance):
            self.ID = ID
            self.balance = balance

        def deposit(self, money):
            if money > 0:
                self.balance += money
                print(f"Вы успешно пополнили счет.Ваш баланс: {self.balance}")

        def withdraw(self, money):
            if money > 0 and money <= self.balance:
                self.balance -= money
                print(f"Вы успешно сняли {money}.Ваш баланс: {self.balance}")
            else:
                print("Недостаточно средств")

        def all_balance(self):
            print(f"Ваш баланс: {self.balance}")

man = Account(1234567, 600)
man.all_balance()
man.withdraw(500)
man.withdraw(700)
man.deposit(23000)

