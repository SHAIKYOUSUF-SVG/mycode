import sys
sys.path.insert(0,"C:\\python\\pycharm\\pytest\\case1\\codes")
from arith1 import *
def test_add1():
    out=add(10,20)
    if out == 30:
        assert True
    else:
        assert False

def test_add2():
    out=add(20,20)
    if out == 40:
        assert True
    else:
        assert False