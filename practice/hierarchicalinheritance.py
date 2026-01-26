#inheritance

class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_name(self):
        print('from main parent cls')
        return self.name
class person1(bank):
    def __init__(self,an,name,salary):
        bank.__init__(self,an,name)
        self.salary=salary
    def get_salary(self):
        return self.salary
class person2(bank):
    def __init__(self,an,name,salary):
        #super().__init__(self,an,name)
        bank.__init__(self,an, name)
        self.salary=salary
    def get_name(self):
        print('from person2 cls')
        super().get_name()
        return self.name



p1=person1(1,"yousuf",100000)
print(p1.get_name())
print(p1.get_salary())

print(p1.name)
p2=person2(2,"esuf",90000)
print(p2.get_name())