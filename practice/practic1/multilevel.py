class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_name(self):
        return self.name

class salarybank(bank):
    def __init__(self,an,name,balance,salary,employee):
        bank.__init__(self,an,name)
        self.salary=salary
        self.balance=balance
        self.employee=employee

    def get_salary(self):
        return self.salary
    def get_balance(self):
        return self.balance

class creditcard(salarybank):
    def withdraw(self,amt):
        if type(amt)!=int or amt<100:
            print('invalidamt')
            return
        if amt>self.balance:
            print("insufficient balance")
            return

        self.balance=self.balance-amt
        return self.balance

c1=creditcard(123,'akhil',5000,50000,'tcs')

c1.withdraw('10000')
print(c1.get_balance())

print(creditcard.mro())