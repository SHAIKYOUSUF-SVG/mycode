'''
using plugins
types of plugins?
    pytest-returnfailures
    pytest-xdist
    pytest-html
    pytest-excel
    pytest-json-report
how get report in html;l format
pip install pytest-excel
pytest   [commnad]
'''

import sys
sys.path.insert(0,r"C:\python\pycharm\pytest\case2\codes")
from arith1 import *
from common1 import *
import pytest

@pytest.mark.anyname
def test_common1():
    x=[10,20,30]
    y=[20,30,50]
    z=common(x,y)
    if z==[20,30]:
        assert True
    else:
        assert False

def test_uniq1():
    x=[10,20,10,10,10]
    y=uniq(x)
    if y==[10,20]:
        assert True
    else:
        assert False,"failing scince not getting uniq numbers"
#deffining class for group of test cases to run at a time
class Test_common1:
    def test_common1(self):
        x=[]
        y=[]
        z=common(x,y)
        if z ==[]:
            assert True
        else:
            assert False

    def test_common2 (self):
        x=[10]
        y=[20]
        z=common(x,y)
        if z==[]:
            assert True
        else:
            assert False

