import pytest
import allure


@allure.title("TC#1 - verify that 8-5 is equal to 3")
@allure.description("This is a smoke Testcase which verify that 8-5 is equal to 3")
@pytest.mark.smoke
def test_subtraction1():
    assert 8 - 5 == 3


@allure.title("TC#2 - verify that 8-8 is equal to 0")
@allure.description("This is a regression Testcase which verify that 8-8 is equal to 0")
@pytest.mark.regression
def test_subtraction2():
    assert 8 - 8 == 0


@allure.title("TC#3 - verify that 8-2 is equal to 6")
@allure.description("This is a smoke Testcase which verify that 8-2 is equal to 6")
@pytest.mark.smoke
def test_subtraction3():
    assert 8 - 2 == 6


@allure.title("TC#4 - verify that 0-0 is not equal to 0")
@allure.description("This is a sanity Testcase which verify that 0-0 is not equal to 0")
@pytest.mark.sanity
def test_subtraction4():
    assert 0 - 0 != 0


@pytest.mark.skip(reason="Not working,Skip it")
def test_subtraction5():
    assert 0 - 0 == 0
