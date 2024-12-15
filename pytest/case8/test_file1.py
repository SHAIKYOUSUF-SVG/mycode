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