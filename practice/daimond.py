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
d1=B()
d1.test()
print(D.mro())


#daimond method

class w:
    def a(self):
        return "w"
class x(w):
    def b(self):
        return "x"
class y(w):
    def c(self):
        return "y"
class z(x,y):
    def d(self):
        return("z")
out=x()
out1=w()
print(w.a(out1))  #calling methods using class name

print(out.b())
