# 5. Invalid Creation - enter a wrong payload or Wrong JSON.


import allure
import pytest
import requests


@allure.title("#TC5 - Invalid creation with wrong payload or wrong JSON")
def test_invalid_creation():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}

    invalid_payload = {
        "firstname": 456,
        "lastname": "Brown",
        "totalprice": "one hundred and eleven",
        "depositpaid": "yes",
        "bookingdates": {
            "checkin": 45/78/888.5,
            "checkout": 45/78/888.5
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=invalid_payload)
    assert response.status_code != 200
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

