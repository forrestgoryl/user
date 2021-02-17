import math
class BankAccount:
    def __init__(self, user_name, account_name, int_rate, balance=0):
        self.user_name = user_name
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance
        if self.balance is float:
            self.balance = round(self.balance, 2)
    
    def deposit(self, amount):
        self.balance += amount
        if self.balance is float:
            self.balance = round(self.balance, 2)
        return self
    
    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        elif self.balance - amount <= 0:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        if self.balance is float:
            self.balance = round(self.balance, 2)
        return self
    
    def display_balance(self):
        return self.balance
    
    def display_info(self):
        print(f"Here is {self.user_name}'s {self.account_name} account: ${self.display_balance()}.")
        return self
    
    def yield_interest(self):
        interest_earned = self.balance*self.int_rate
        self.balance += interest_earned
        if self.balance is float:
            self.balance = round(self.balance, 2)
        print(f"Your account yielded interest: you earned ${interest_earned}. Your balance is now ${self.balance}.")
        return self
    
    def transfer_money(self, other_user, amount):
        self = self.withdrawal(amount)
        other_user = other_user.deposit(amount)
        print(f"Transferred money from {self.user_name} to {other_user.user_name}.")
        return self