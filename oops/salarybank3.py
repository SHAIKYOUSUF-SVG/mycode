import re
from Bank1 import bank
class salaryBank(bank):
    def __init__ (self,an,name,bank,balance,emp,salary):
        bank.__init__(self,an,name,bank,balance)
        self.emp=emp
        self.salary=salary
    def get_salary(self):
        return self.salary
    def deposit(self,amt):
        if type(amt) != int:
            return True
        if amt <100:
            print("minimum amount must be 100")
            return True
        self.balance=self.balace+amt
    def withdraw(self,amt):
        if type(amt) !=int:
            return True
        if amt <100:
            print("minimum amt must above 100")
            return True
        if amt > self.balance:
            print("insufficient balance")
            return True
        self.balance=self.balance-withdraw