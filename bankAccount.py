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
        print(f"This is a {self.int_rate * 100}% account and the balance is ${self.balance}.")
        return self
    
    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        if self.balance is float:
            self.balance = round(self.balance, 2)
        return self

Forrest = BankAccount(0.01, 50)
Serena = BankAccount(0.05, 2000)

Forrest.deposit(50).deposit(200).deposit(1000).withdrawal(200).display_info().yield_interest().display_info()
Serena.deposit(200).deposit(200).withdrawal(50).withdrawal(100).withdrawal(50).withdrawal(200).display_info().yield_interest().display_info()
