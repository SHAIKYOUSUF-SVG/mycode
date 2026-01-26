class bank:
    counter=0
    def __init__(self,an,name):
        self.an=an
        self.name=name
        self.counter+=1
    def get_counter1(self):
        return bank.counter
    @classmethod
    def get_counter2(cls):
        print('cls method',cls)
        return bank.counter
    # def get_counter2(self):
    #     print('cls method',self)
    #     return bank.counter
b1=bank(123,'sachin')
b2=bank(124,'kiran')

print(b1.get_counter1())
print(bank.get_counter1(b1))
print(b2.get_counter2())


class info:
    candidate='person1'
    def __init__(self,name,age,bg):
        self.name=name
        self.age=age
        self.bg=bg
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    @classmethod
    def get_bg(cls):
        return info.candidate

c1=info('esuf',27,'o-psitive')
c2=info('yousuf',23,'a-positive')

print(c1.get_name())
print(c1.get_bg())
print(c1.__dict__)
