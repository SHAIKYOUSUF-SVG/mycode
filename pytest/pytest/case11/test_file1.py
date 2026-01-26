'''what is parametrize?
used to decress the no.of modules
we have to write 1 module and with different paramites in form of list
@pytest.parametrize()

@pytest.mark.parametrize("x,y,z",[(1,2,3),(2,5,7),(4,6,10)])
'''
import pytest

def add(x,y):
    return x+y
@pytest.mark.parametrize("x,y,z",[(1,2,3),(2,5,7),(4,6,10)])
def test(x,y,z):
    out=add(x,y)
    if out==z:
        assert True
    else:
        assert False