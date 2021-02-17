import math
class BankAccount:
    def __init__(self, int_rate, balance=0):
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
    
    def display_info(self):
        return self.balance
    
    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        if self.balance is float:
            self.balance = round(self.balance, 2)
        return self