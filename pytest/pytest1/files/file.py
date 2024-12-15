import pytest
import sys
sys.path.insert(0,r"C:\python\pycharm\pytest\case2\codes")
from common1 import *


def yousuf():
    #log.info("this is about testcases")
    x=[10,20,30]
    y=[20,30,50]
    z=common(x,y)
    if z==[20,30]:
        assert True
    else:
        assert False

def me():
    x=[10,20,30]
    y=[20,30,50]
    z=common(x,y)
    if z==[20,30]:
        assert True
    else:
        assert False