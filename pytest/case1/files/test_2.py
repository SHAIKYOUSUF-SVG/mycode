import pytest


@pytest.mark.order(2)
def test1_1():
    assert True


@pytest.mark.order(3)
def test1_2():
    assert True


@pytest.mark.order(4)
def test1_3():
    assert True


@pytest.mark.order(1)
def test1_4():
    assert True
