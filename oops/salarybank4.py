import re
from Bank1 import bank
class salaryBank(bank):
    def __init__ (self,an,name,branch,balance,emp,salary):
        bank.__init__(self,an,name,branch,balance)
        self.emp=emp
        self.salary=salary
    def get_salary(self):
        return self.salary
    @staticmethod
    def not_valid_amt(amt):
        if type(amt) != int:
            return True
        if amt <100:
            print("minimum amount must be 100")
            return True
    def deposit(self,amt):
        if self.not_valid_amt(amt):
            return


        self.balance=self.balance+amt
    def withdraw (self,amt):
        if self.not_valid_amt(amt):
            return
        if amt > self.balance:
            print("insufficient balance")
            return True
        self.balance=self.balance-amt


s1=salaryBank(123,"kiran","pdrl",900,"abc",90000)
print(s1.get_salary())
print(s1.balance)
s1.deposit(1000)
print(s1.balance)

s1.withdraw(500)
print(s1.balance)