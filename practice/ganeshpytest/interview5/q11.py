#multi level inheritance?


class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_name(self):
        print("from bank")
        return self.name
    def get_an(self):
        print("from bank")
        return self.an
class creaditcard:
    def get_credit_limt(self):
        return 50000
    def get_an(self):
        print("fron creditcard")
        return self.an

class savingsbank(bank,creaditcard):
    def get_an(self):
        print("from savings bank")
        super().get_an()  #super() used to set search order
        return self.an

s1=savingsbank(123,"kiran")
print(s1.get_an())
print(s1.get_name())

#multi level inheritance means 2 parent class an 1 child class ccessing propeties of
#2 parent classes from child class
#if not found in 1 parent class then it will search in another parent class