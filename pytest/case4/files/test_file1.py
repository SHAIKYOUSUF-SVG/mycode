#how to run marked test cases only
#@pytest.mark.anyname
#nedd to wrote import pytest also

import pytest
import sys
sys.path.insert(0,r"C:\python\pycharm\pytest\case2\codes")
from arith1 import *


@pytest.mark.anyname
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
'''
def list(obj):
    list1=[]
    for i in obj:
        if i not in list:
            list.append((i))
    return list1
def test_list():
    out=list(1,2,3,4,5)
    if list1 ==[1,2,3,4,5]:
        assert True
    else:
        assert False'''

def squares(obj):
    mylist=[]
    for i in obj:
        mylist.append(i*i)
    return mylsit
def test_squares():
    out1=mylist(2,3,4,5)
    if mylist==[4,6,16,25]:
        assert True
    else:
        assert False