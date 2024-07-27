import pytest
import allure
import requests


@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Pramod Dutta")
@allure.testcase("TC#5")
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200
