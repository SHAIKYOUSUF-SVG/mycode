#what is polymorphism:
#based on object,methods will be called
#to define methods in child class with thw same name as defined in their parent class

class bank:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.balance=balance
        self.account_type="primary"
    def get_name(self):
        return self.name
    def get_account_type(self):
        return self.account_type
class salarybank:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.balance=balance
        self.account_type="secondary"
    def get_name(self):
        return self.name
    def get_account_type(self):
        return self.account_type

b1=bank(123,"a",900)
s1=salarybank(122,"b",800)

out=s1.get_account_type()
out1=b1.get_account_type()
print(out)
print(out1)

#method will be called based on object

#polymorphism with out using constructer[__init__]
class bank:
    def start(self,an,name):
        self.an=an
        self.name=name
    def get_name(self):
        print("from main bank")
        return self.name
class salarybank(bank):
    def start(self,an,name):
        self.an=an
        self.name=name
    def get_name(self):
        print("from salarybank")
        return self.an
b1=bank()
b1.an=132
b1.name="kiran"
print(b1.get_name())


s1=salarybank()
s1.an=122
s1.name="rsvi"
print(s1.get_name())