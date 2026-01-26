class bank:
    def __init__(self,an,name,branch,balance):
        self.__an=an
        self.__name=name
        self.__branch=branch
        self.__balance=balance
    def get_an(self):
        return self.__an
    def __get_name(self):
        return self.__name
class salarybank(bank):
    def __init__(self,an,name,branch,balance,salary):
        bank.__init__(self,an,name,branch,balance)
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_balance(self,amt):
        if type(amt)==int:
            self.balance=self.balance+amt
class creditcard(salarybank):
    def __init__(self,an,name,branch,balance,salary,creditlimit):
        salarybank.__init__(self,an,name,branch,balance,salary)
        self.__creditlimit=creditlimit
    def __get_creditlimit(self):
        return self.__creditlimit
    def __get_name(self):
        return self.__name
output=creditcard(123,"yousuf","pdrl",0,70000,100000)
# print(output.get_an())
# print(output.get_creditlimit())


print(output._creditcard__get_creditlimit())
print(output._creditcard__creditlimit)
print(output._bank__name)

b=bank(111,"esuf","pdrl",0)
print(b._bank__get_name())
print(b._bank__an)

class bank:
    Bank="SBI"
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
    @classmethod
    def get_bank(cls):
        return bank.Bank
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def squares(*args):
        l=[]
        for i in args:
            if i%2==0:
                l.append(i)
        return l
    @staticmethod
    def check_prime():
        k=True
        num=10
        for i in range(2,num):
            if num%i==0:
                k=False
                print(f"{num} is not a prime")
                exit()
        if k:
            return num
out=bank(123,'yousuf','pdrl',200)
if __name__=="__main__":

    print(out.get_bank())
    print(out.add(100,10))
    print(out.squares(1,2,3,4,5,6,7,8,9,10))
    print(out.check_prime())