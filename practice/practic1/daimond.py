class A:
    def test(self):
        print('A')

class B(A):
    def test(self):
        print('B')
class C(A):
    def test(self):
        print('C')
class D(B,C):
    def test(self):
        print('D')
dd=D()
print(dd.test())


print(D.mro())