class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        """Метод для поповнення рахунку"""
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено на {amount} грн.")
        else:
            print("Сума поповнення має бути додатною!")

    def withdraw(self, amount):
        """Метод для зняття коштів"""
        if amount <= 0:
            print("Сума зняття має бути додатною!")
        elif amount > self.__balance:
            print(f"Недостатньо коштів! Ваш баланс: {self.__balance} грн.")
        else:
            self.__balance -= amount
            print(f"Знято {amount} грн.")

    def get_balance(self):
        """Публічний метод для перегляду балансу (getter)"""
        return self.__balance

account = BankAccount("Олексій", 1000)
print(f"Початковий баланс: {account.get_balance()} грн")
account.deposit(500)   
account.withdraw(200)  
print(f"Поточний баланс: {account.get_balance()} грн")

print("-" * 30)

print("Спроба змінити баланс напряму (account.__balance = 1000000):")
try:
    account.__balance = 1000000 
    print(account.__balance) 
except AttributeError:
    print("Помилка! Немає доступу до приватного атрибуту '__balance'.")
print(f"\nРеальний баланс після спроби злому: {account.get_balance()} грн")