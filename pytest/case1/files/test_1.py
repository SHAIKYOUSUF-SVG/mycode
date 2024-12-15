import pytest

@pytest.mark.regression
def test1_1():
    assert True
@pytest.mark.perf
def test2_1():
    assert True

@pytest.mark.xfail
def test3_1():
    assert True

@pytest.mark.skip
def test4_1():
    assert True
'''
@pytest.mark.parametrize("a,b,expected",[1,3,4])
def test5_1(a,b,expected):
    assert a+b==expected'''


@pytest.mark.parametrize("str1", ["python"])
def test6_1(str1):
    assert len(str(str1)) == 6


@pytest.mark.parametrize('str3,expected',["python", 6])
def test6_1(str3,expected):
    assert len(str3) ==expected