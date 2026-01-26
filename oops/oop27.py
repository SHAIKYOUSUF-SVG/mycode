#making class attributes privates


class bank:
    __counter=0
    def __init__(self,an):
        self.an=an
        bank.__counter +=1
class salarybank(bank):
    def test(self):
        print(bank.__counter)

b1=salarybank(123)
b2=salarybank(124)

b2.test()

