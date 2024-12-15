class bank:
    counter=0
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_an(self):
        return self.an
    @staticmethod
    def mul(x,y):
        return x*y

b1=bank(123,'sachin')
print(bank.mul(10,10))

class bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
    def get_an(self):
        return self.an
    def get_branch(self):
        return self.branch
    def get_balance(self):
        return self.balance

class salarybank(bank):
    def __init__ (self,an,name,branch,balance,emp,salary):
        bank.__init__(self,an,name,branch,balance)
        self.emp=emp
        self.salary=salary
    def get_salary(self):
        return self.salary
    @staticmethod
    def not_valid_amt(amt):
        if type(amt)!=int:
            print('invalid amt')
            return True
        if amt<100:
            print('minimum amount above 100')
            return True
    def deposit(self,amt):
        if self.not_valid_amt(amt):
            return
        self.balance=self.balance+amt
    def withdraw(self,amt):
        if self.not_valid_amt(amt):
            return
        self.balance=self.balance-amt


s1=salarybank(123,'ramesh','HSR',5000,'TCS',40000)
print(s1.get_balance())

s1.deposit('abc')