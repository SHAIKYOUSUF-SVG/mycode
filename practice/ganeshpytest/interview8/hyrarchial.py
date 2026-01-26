#hyrarchial inheritance:

class bank:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.balance=balance
    def get_balance(self):
        return self.balance
    def set_balance(self,amt):
        self.balance=amt

class savingsbank(bank):
    def withdraw (self,amt):
        if amt >10000:
            print("##min 10000 only##")
            return
        self.balance=self.balance-amt
class businessbank(bank):
    def withdraw(self,amt):
        if amt >100000:
            print("##min 100000 onoly##")
            return
        self.balance=self.balance-amt
class creditcardbank(savingsbank):
    def pay_bill(self):
        self.balance=self.balance-1000
        print("payment successfull")

b1=businessbank(123,"rakesh",800900)
out=b1.get_balance()
print(businessbank.mro())
print(out)

b1.withdraw(100)
print(b1.__dict__)
b1.withdraw(90000)
print(b1.get_balance())

print(creditcardbank.mro())

c1=creditcardbank(122,"rajesh",80000)
c1.withdraw(12000)
print(c1.get_balance())