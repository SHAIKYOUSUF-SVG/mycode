from Bank import bank  #bank is module its only functions

#xlass salarybank(BAnk.bank) differnet types to load module[arith.add]
class salarybank(bank):
    def deposit(self,amt):
        if amt <100:
            print("amount must be aboue hundred")
            return
        if type(amt) != int:
            print("unable to access")
            return

        self.balance=self.balance+amt
    def withdraw(self,amt):
        if amt <100:
            print("amount must be abouve 100")
            return
        if type(amt)!=int:
            print("invalid amount")
            return
        if amt > self.balance:
            print("insufficient amount")
            return
        self.balance=self.balance-amt