#MRO-method resolution order
#base/top class for any for any class in p[ython is -object class
#in which order the programe is going to serach



class A:
    def test(self):
        print("A")
class B(A):
    def test(self):
        print("B")
class C(A):
    def test(self):
        print("C")
class D(B,C):
    def test(self):
        print("D")

d1=D()
#d1.test()
print(D.mro())