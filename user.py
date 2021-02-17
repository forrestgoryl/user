import bankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount.BankAccount(0.02, balance=0)
    
    def make_withdrawal(self, amount):
        self.account = self.account.withdrawal(amount)
        print(f"{self.name} withdrew ${amount}. Balance is {self.account.display_info()}.")
        return self

    def make_deposit(self, amount):
        self.account = self.account.deposit(amount)
        print(f"{self.name} made a deposit of ${amount}.")
        return self
    
    def display_user_balance(self):
        print(f"Here is {self.name}'s balance: {self.account.display_info()}.")
        return self

    def transfer_money(self, other_user, amount):
        self.account = self.account.withdrawal(amount)
        other_user.account = other_user.account.deposit(amount)
        print(f"Transfered ${amount} from {self.name} to {other_user.name}.")
        return self

Greg = User("Greg", "greg@gmail.com")
Forrest = User("Forrest", "forrest@outlook.com")
Serena = User("Serena", "serena@qq.com")

Greg.make_deposit(50).make_deposit(100).make_deposit(30).make_withdrawal(20)
Forrest.make_deposit(50).make_deposit(200).transfer_money(Serena, 50)
Serena.make_deposit(300).make_withdrawal(100)