
#how to run all testcases from a folder
import sys
sys.path.insert(0,f"C:\python\pycharm\pytest\pytest\case1\codes")
from arith1 import *
from common1 import *

class Testcommon:
    def test_c3(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 3, 5, 6]
        l3 = common(l1, l2)
        if l3 == [1, 3]:
            assert True
        else:
            assert False

    def test_c4(self):
        l1 = []
        l2 = []
        l3 = common(l1, l2)
        if l3 == []:
            assert True
        else:
            assert False