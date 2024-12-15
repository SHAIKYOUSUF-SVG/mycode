'''
what is mro?
method resolution order
search process will done in a order as we worte
top class/object from any class in  pyhton is object clsss ?????????????????
'''

class A:

    def test(self):
        print("A")
class B(A):
    def test2(self):
        print("B")
class C(A):
    def test3(self):
        print("C")
class D(B,C):
    def test4(self):
        print("D")

d1=D()
d1.test()
d1.test2()
d1.test3()
d1.test4()






