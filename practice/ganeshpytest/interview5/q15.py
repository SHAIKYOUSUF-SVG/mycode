#super():is a function to call methods from parent class(parent cls will be serah in mro order)
#mro order: d then b then c then a


class A:
    def test(self):
        print("A")
class B(A):
    def test(self):
        super().test()  #parent class will search in mro order only
        print("B")
class C(A):
    def test(self):
        print("C")
class D(B,C):
    def test(self):
        super().test()  #
        print("D")

d1=D()
d1.test()
