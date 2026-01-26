class bank:
    counter=0
    def __init__(self,an):
        self.an=an
        bank.counter+=1
        print(bank.counter)
class salarybank(bank):
    def test(self):
        print("is",bank.counter)
b1=bank(111)
s1=salarybank(123)
s2=salarybank(122)


s1.test()