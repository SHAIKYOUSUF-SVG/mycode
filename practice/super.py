'''
what is super()?
super():is a method used to 'access  methods or attributes' from parent class in order to
modify the behaviour in the child class
parent class process according to mro method
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
        super().test()
        print("D")

d1=D()
d1.test()