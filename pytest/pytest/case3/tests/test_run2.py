import sys
sys.path.insert(0,f"C:\python\pycharm\pytest\pytest\case1\codes")
from arith1 import *
from common1 import *


def abc_common1():
    x=[10,20,30]
    y=[10,40]
    z=common(x,y)
    if z==[10]:
        assert True
    else:
        assert False

def xy_uniq1():
    list=[1,2,3,4,2,1,2,3,2]
    z=uniq(list)
    if z==[1,2,3,4]:
        assert True
    else:
        assert False
#guoup test cases/bunch of test cases using class
class Testcommon:   #test suit
    def test_c1(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 3, 5, 6]
        l3 = common(l1, l2)
        if l3 == [1, 3]:
            assert True
        else:
            assert False

    def test_c2(self):
        l1 = []
        l2 = []
        l3 = common(l1, l2)
        if l3 == []:
            assert True
        else:
            assert False



    
