# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

import allure
import pytest
import requests


@pytest.fixture()
@allure.title("Create a new booking")
def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Created Booking ID: {booking_id}")
    return booking_id


@allure.title("#TC1 -Verify that firstName is updated or not")
@pytest.mark.integration
def test_create_and_patch_booking(create_booking, create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)
    PATCH_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    patch_payload = {
        "firstname": "Vimal",
    }

    patch_response = requests.patch(url=PATCH_URL, headers=headers, json=patch_payload)
    assert patch_response.status_code == 200
    assert "application/json" in patch_response.headers["Content-Type"]
    patched_data = patch_response.json()
    assert patched_data["firstname"] == "Vimal"
    print(f"Patched Booking Data: {patched_data}")

    get_response = requests.get(url=PATCH_URL)
    assert get_response.status_code == 200
    assert "application/json" in get_response.headers["Content-Type"]
    get_data = get_response.json()
    assert get_data["firstname"] == "Vimal"
    print(f"Verified Patched Booking Data: {get_data}")



