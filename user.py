class User:
    def __init__(self, name, email, account_balance=0):
        self.name = name
        self.email = email
        self.account_balance = account_balance
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def display_user_balance(self):
        print(f"Here is {self.name}'s balance: {self.account_balance}.")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Greg = User("Greg", "greg@gmail.com")
Forrest = User("Forrest", "forrest@outlook.com")
Serena = User("Serena", "serena@qq.com")

Greg.make_deposit(50).make_deposit(100).make_deposit(30).make_withdrawal(20)
Forrest.make_deposit(50).make_deposit(200).transfer_money(Serena, 50)
Serena.make_deposit(300).make_withdrawal(100)

print(f"""Greg's balance is {Greg.account_balance}. Forrest's balance is {Forrest.account_balance}. 
Serena's balance is {Serena.account_balance}.""")