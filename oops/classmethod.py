'''
methods class method obejct method,static method
'''

#class method

class bank:
    counter=0
    def __init__(self,an):
        self.an=an
        bank.counter +=1
        #self.counter+=1

    def get_method1(self):
        print(self)
        return self.counter
    @classmethod
    def get_method2(self):
        print("class method",self)
        return bank.counter
b1=bank(123)
b2=bank(122)


print(b1.get_method1())

print("#####################")
print(b1.get_method2())
print(bank.get_method2())

fw=open("staticmethod.py", "w")
fw.close()