class bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
    def get_name(self):
        return self.name
    def get_branch(self):
        return self.branch
class salarybank:
    def __init__(self,an,name,branch,balance,salary,employee):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
        self.salary=salary
        self.employee=employee

class me(bank,salarybank):
    def __init__(self,an,name,branch,balance,salary,employee):
        #bank.__init__(self,an,name,branch,balance)
        salarybank.__init__(self,an,name,branch,balance,salary,employee)
    def get_an(self):
        return self.an

p=me(123,"yousuf","pdrl",0,70000,'tcs')
print(p.get_an())