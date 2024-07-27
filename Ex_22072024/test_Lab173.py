import pytest


@pytest.mark.smoke
def test_subtraction1():
    assert 8 - 5 == 3


@pytest.mark.regression
def test_subtraction2():
    assert 8 - 8 == 0


@pytest.mark.smoke
def test_subtraction3():
    assert 8 - 2 == 6


@pytest.mark.sanity
def test_subtraction4():
    assert 0 - 0 == 0


@pytest.mark.skip(reason="Not working,Skip it")
def test_subtraction5():
    assert 0 - 0 == 0
