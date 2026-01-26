class bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
    def get_an(self):
        return self.an
    def get_name(self):
        return self.name
class salarybank(bank):
    def __init__(self,an,name,branch,balance,salary):
        bank.__init__(self,an,name,branch,balance)
        self.salary=salary
    def get_salary(self):
        return self.salary
    def set_balance(self,amt):
        if type(amt)==int:
            self.balance=self.balance+amt
class creditcard(salarybank):
    def __init__(self,an,name,branch,balance,salary,creditlimit):
        salarybank.__init__(self,an,name,branch,balance,salary)
        self.creditlimit=creditlimit
    def get_creditlimit(self):
        return self.creditlimit
output=creditcard(123,"yousuf","pdrl",0,70000,100000)
print(output.get_an())
print(output.get_creditlimit())
