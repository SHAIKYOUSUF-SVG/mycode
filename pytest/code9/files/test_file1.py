import pytest,sys
sys.path.insert(0,'C:\\python\\pycharm\\pytest\\code9\\codes')
import arith1
from arith1 import *
def test_add():
    out=add(10,10)
    if out==20:
        assert True
    else:
        assert False