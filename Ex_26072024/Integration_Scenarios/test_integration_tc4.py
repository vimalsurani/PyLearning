# 4. Create a BOOKING, Delete It


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


@allure.title("#TC4 - Create a booking and delete it")
@pytest.mark.integration
def test_create_and_delete_booking(create_token, create_booking):
    booking_id = create_booking
    base_url = "https://restful-booker.herokuapp.com/"
    DELETE_URL = base_url + str(booking_id)

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    # Delete the booking
    delete_response = requests.delete(url=DELETE_URL, headers=headers)
    assert delete_response.status_code == 404
    print(f"Deleted Booking ID: {booking_id}")

    # Verify that the booking is deleted
    get_response = requests.get(url=DELETE_URL)
    assert get_response.status_code == 404
    print(f"Verified deletion of Booking ID: {booking_id}")
