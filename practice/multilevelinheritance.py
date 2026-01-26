'''
acesseing 1 child class from another child class
process of deriving 1 child class from anther derived child class or from another derived child class
class A:
class B(A):
class C(B):
'''

#multilevelinheritance


class bank:
    def __init__(self, an, name, balance):
        self.an = an
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance


class savingsbank(bank):

    def withdraw(self, amt):
        # super().get_balance()
        if type(amt) == int and amt > 10000:
            print("amount must be less than 10k")
            return
        self.balance = self.balance - amt


class creditcardbank(savingsbank):
    def withdraw(self, amt):
        if amt > 100000:
            print("min amount lessthan 100000")
            return
        self.balance = self.balance - amt


c1 = creditcardbank(123, "rajesh", 9000000)
print(c1.get_balance())
c1.withdraw(10000)
print(c1.__dict__)

s1 = savingsbank(124, "rakesh", 100000)
out = s1.get_balance()
print(out)
s1.withdraw(5000)
print(s1.__dict__)
###########################################################

class A:
    def __init__(self, arg1):
        self.arg1 = arg1


class B(A):
    def __init__(self, arg2):
        self.arg2 = arg3
        super().__init__(arg1)


class C(B):
    def __init__(self, arg3):
        self.arg3 = arg3
        super().__init__(arg1, arg2)


class D(C):
    def __init__(self, arg4):
        self.arg4 = arg4
        super().__init(arg1, arg2, arg3)


d1 = D("a", "b", "c", "d")

###################################################################
class server:
    def __init__(self,bmc,bios,cpld):
        self.bmc=bmc
        self.bios=bios
        self.cpld=cpld
    def get_bios(self):
        return self.bios
    def get_bmc(self):
        return self.bmc
    def get_cpld(self):
        return self.cpld
class storage(server):
    def __init__(self,bmc,bios,cpld,psus,ioms):
        server.__init__(self,bmc,bios,cpld)
        self.ioms=ioms
        self.psus=psus
class desktop(server):
    def __init__(self,bmc,bios,cpld,os):
        server.__init__(self,bmc,bios,cpld)
        self.os=os
    def get_os(self):
        return self.os
d1=desktop("bmc12","bios12","cpld12","widows11")

print(d1.get_os())

print(d1.bmc)