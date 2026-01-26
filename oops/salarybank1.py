from Bank import bank

class salarybank(bank):
    def __init__(self,an,name,branch,balance,emp,salary):
        self.an = an
        self.name = name
        self.branch = branch
        self.balance = balance
        self.emp=emp
        self.salary=salary
    def get_salary(self):
        return self.salary

    def deposite(self,amt):
        if type(amt) != int:
            print(f"invalid amount {amt}")
            return
        if amt < 100:
            print("unable to access")
            return
        self.balance=self.balance+amt
    def withdraw(self,amt):
        if type(amt) != int:
            print(f"invalid amount {amt}")
            return
        if amt < 100:
            print("unable to access")
            return
        if amt >self.balance:
            print(f"insufficiant amount {amt}")
            return
        self.balance=self.balance-amt
