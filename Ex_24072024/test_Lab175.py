import pytest
import allure
import requests


@allure.title("Test GET Request - Restful Booker - Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID")
@allure.tag("Regression", "P0", "Smoke")
@allure.label("Owner", "Vimal Surani")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200


@allure.title("Test GET Request - Restful Booker - Project#1")
@allure.description("TC#2 -> Verify that GET Request with Invalid BookingID")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404


@allure.title("Test GET Request - Restful Booker - Project#1")
@allure.description("TC#3 -> Verify that GET Request with Invalid BookingID")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404
