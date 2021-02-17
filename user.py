import bankAccount
class User:
    def __init__(self, name, *account_name):
        self.name = name
        self.account = {}
        for i in range(len(account_name)):
            self.account[account_name[i]] = bankAccount.BankAccount(self.name, account_name[i], int_rate=0.02, balance=0)    

Greg = User("Greg", "BankOfAmerica", "CreditUnion")
Forrest = User("Forrest", "BankOfChina", "PayPal")






Greg.account["BankOfAmerica"].deposit(50).deposit(100).withdrawal(20).deposit(80).display_info()
Greg.account["CreditUnion"].deposit(500).withdrawal(100).deposit(50).display_info()
Forrest.account["BankOfChina"].deposit(500).display_info()
Greg.account["CreditUnion"].transfer_money(Forrest.account["BankOfChina"], 50)
Forrest.account["BankOfChina"].display_info()