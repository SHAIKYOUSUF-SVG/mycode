class test:
    def A(self):
        print('a')
class test1(test):
    def B(self):
        print('b')
class test2(test):
    def C(self):
        print('c')
class test3(test2,test1):
    def D(self):
        print('d')
t=test1()
#t.A()
t.B()
