#daimond problem:
'''
    A
B       C
    D
'''

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
d1.test()