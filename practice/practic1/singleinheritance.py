class bank:
    def __init__(self,an,name):
        self.name=name
        self.an=an
    def get_an(self):
        return self.an
class salarybank(bank):
    def __init__(self,an,name,salary,balance):
        super().__init__(an,name)
        self.salary=salary
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    @staticmethod
    def func(amt):
        if type(amt)!=int or amt<0:
            print('invalid amt')
            return True
        if amt<100:
            return True

    def diposit(self,amt):
        if self.func(amt):
            print('error')
            return

        if amt>=100000:
            print('minimu amount should be below 100000')
            return
        self.__balance=self.__balance+amt
    def withdraw(self,amt):
        if self.func(amt):
            print('error')
            return
        self.__balance=self.__balance-amt
s1=salarybank(123,'rajesh',90000,100000)
print(s1.get_balance())
s1.diposit('800')
print(s1.get_balance())
s1.withdraw(700)
print(s1.get_balance())


class bank:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def diposit(self,amt):
        if type(amt)!=str or amt<100:
            print('invalid amt')
            return
        self.__balance=self.__balance+amt
    def withdraw(self,amt):
        if type(amt)!=str or amt<100:
            print('invalid amt')
            return
        self.__balanace=self.__balance-amt

a=bank(111,'aaa',900)
a.diposit(1)
print(a.get_balance())