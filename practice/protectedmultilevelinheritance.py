class bank:
    def __init__(self,an,name,branch,balance):
        self._an=an
        self._name=name
        self._branch=branch
        self._balance=balance
    def _get_an(self):
        return self._an
    def _get_name(self):
        return self._name
class salarybank(bank):
    def __init__(self,an,name,branch,balance,salary):
        bank.__init__(self,an,name,branch,balance)
        self._salary=salary
    def get_salary(self):
        return self._salary
    def set_balance(self,amt):
        if type(amt)==int:
            self._balance=self._balance+amt
class creditcard(salarybank):
    def __init__(self,an,name,branch,balance,salary,creditlimit):
        salarybank.__init__(self,an,name,branch,balance,salary)
        self._creditlimit=creditlimit
    def _get_creditlimit(self):
        return self._creditlimit
output=creditcard(123,"yousuf","pdrl",90,70000,100000)
print(output._get_an())
print(output._get_creditlimit())
print(output._get_name())

print(output._balance)

print(output._branch)

print(output.get_salary())

print(output._get_an())

output.set_balance(120000)
print(output.__dict__)


