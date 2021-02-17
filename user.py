class User:
    def __init__(self, name, email, account_balance=0):
        self.name = name
        self.email = email
        self.account_balance = account_balance
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def display_user_balance(self):
        print(f"Here is {self.name}'s balance: {self.account_balance}.")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Greg = User("Greg", "greg@gmail.com")
Forrest = User("Forrest", "forrest@outlook.com")
Serena = User("Serena", "serena@qq.com")

print(Greg.account_balance, Forrest.account_balance, Serena.account_balance)
Greg.make_deposit(50)
Serena.make_deposit(150)
Forrest.make_deposit(50)
print(Greg.account_balance, Forrest.account_balance, Serena.account_balance)
Serena.transfer_money(Forrest, 50)
print(Greg.account_balance, Forrest.account_balance, Serena.account_balance)