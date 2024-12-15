#based on object ,right method will be called

class Account:
    def __init__(self,an,name):
        self.an=an
        self.name=name
        self.account_type="general"
    def get_account_type(self):
        return self.account_type

class primeaccount:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.balance=balance
        self.prime_account_type="prime acc"
    def get_account_type(self):
        return self.prime_account_type

obj1=Account(123,"rakesh")
obj2=primeaccount(122,"rajesh",200)
out=obj2.get_account_type()
print(out)