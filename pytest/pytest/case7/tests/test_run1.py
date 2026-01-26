#how to mark tests cases
import sys
import pytest
sys.path.insert(0,r"C:\python\pycharm\pytest\pytest\case1\codes")
from arith1 import *
from common1 import *
@pytest.mark.slow
def test_add1():  #test write manadatory for test case
    out=add(10,10)
    if out== 20:
        assert True
    else:
        assert False
@pytest.mark.slow
def test_add2():
    out=add(10,19)
    if out==29:
        assert True
    else:
        assert False
